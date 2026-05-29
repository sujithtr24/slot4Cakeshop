from django.test import TestCase
from django.urls import reverse
from customerapp.models import customer_tbl

class AdminCustomerEditTests(TestCase):
    def setUp(self):
        # Create a test customer
        self.customer = customer_tbl.objects.create(
            customer_name="John Doe",
            customer_email="john@example.com",
            customer_phone=1234567890,
            customer_password="testpassword123"
        )
        self.edit_url = reverse('adminEditCustomer', args=[self.customer.id])
        self.list_url = reverse('adminCustomers')

    def test_edit_customer_get(self):
        """Test GET request to edit page loads customer details correctly"""
        response = self.client.get(self.edit_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin/admin-editCustomer.html')
        self.assertContains(response, self.customer.customer_name)
        self.assertContains(response, self.customer.customer_email)
        self.assertContains(response, str(self.customer.customer_phone))
        # Verify Customer ID is readonly or has readonly attribute in HTML
        self.assertContains(response, 'readonly')

    def test_edit_customer_post(self):
        """Test POST request successfully updates customer and redirects"""
        updated_data = {
            'customer_name': 'John Edited',
            'customer_email': 'john_edited@example.com',
            'customer_phone': '9876543210'
        }
        response = self.client.post(self.edit_url, data=updated_data)
        
        # Verify redirect to customer list page
        self.assertRedirects(response, self.list_url)
        
        # Verify database updated
        self.customer.refresh_from_db()
        self.assertEqual(self.customer.customer_name, 'John Edited')
        self.assertEqual(self.customer.customer_email, 'john_edited@example.com')
        self.assertEqual(self.customer.customer_phone, 9876543210)

    def test_edit_non_existent_customer(self):
        """Test editing a customer ID that doesn't exist raises DoesNotExist"""
        with self.assertRaises(customer_tbl.DoesNotExist):
            self.client.get(reverse('adminEditCustomer', args=[99999]))

    def test_delete_customer(self):
        """Test deleting a customer removes them from database and redirects"""
        delete_url = reverse('adminDeleteCustomer', args=[self.customer.id])
        response = self.client.get(delete_url)
        self.assertRedirects(response, self.list_url)
        
        # Verify customer no longer exists in database
        with self.assertRaises(customer_tbl.DoesNotExist):
            customer_tbl.objects.get(id=self.customer.id)

