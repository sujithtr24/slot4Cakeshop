from django.db import models
from adminapp.models import cake_tbl

# Create your models here.
class customer_tbl(models.Model):
    customer_name = models.CharField(max_length=50)
    customer_email = models.EmailField()
    customer_phone = models.PositiveIntegerField()
    customer_password = models.CharField(max_length=20)

class cart_tbl(models.Model):
    customer = models.ForeignKey(customer_tbl, on_delete=models.CASCADE)
    cake = models.ForeignKey(cake_tbl, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_amount(self):
        return self.quantity * self.cake.cake_price