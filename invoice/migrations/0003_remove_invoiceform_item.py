# Generated by Django 4.1 on 2022-08-31 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0002_itemform_remove_invoiceform_date_created_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoiceform',
            name='item',
        ),
    ]
