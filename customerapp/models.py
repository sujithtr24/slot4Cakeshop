from django.db import models

# Create your models here.
class customer_tbl(models.Model):
    customer_name = models.CharField(max_length=50)
    customer_email = models.EmailField()
    customer_phone = models.PositiveIntegerField()
    customer_password = models.CharField(max_length=20)