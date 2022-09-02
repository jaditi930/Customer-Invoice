from django.db import models

# Create your models here.
class InvoiceForm(models.Model):
    name=models.CharField(max_length=100,null=True)
    email=models.EmailField(max_length=100,null=True)
    phone=models.BigIntegerField(null=True)
    itemname=models.TextField(null=True)
    quantity=models.TextField(null=True)
    price=models.TextField(null=True)
    category = models.TextField(null=True)





     
