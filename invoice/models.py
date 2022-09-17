from django.db import models

# Create your models here.
class InvoiceForm(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.BigIntegerField()
    itemname=models.TextField()
    quantity=models.TextField(default=1)
    price=models.TextField()
    category = models.TextField()





     
