# Generated by Django 4.0.7 on 2022-09-16 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0009_alter_invoiceform_category_alter_invoiceform_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoiceform',
            name='quantity',
            field=models.TextField(default=1),
        ),
    ]
