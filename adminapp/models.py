from django.db import models

# Create your models here.
class cake_tbl(models.Model):
    CATEGORY_CHOICES =[
        ('vanila','vanila'),
        ('chocolate','chocolate'),
        ('starwberry','starwberry'),
        ('others','others')
    ]

    cake_name = models.CharField(max_length=50)
    cake_price = models.PositiveIntegerField()
    cake_description = models.TextField(blank=True)
    cake_category = models.CharField(choices=CATEGORY_CHOICES, default='others', max_length=20)
    cake_image = models.FileField(upload_to='pictures')