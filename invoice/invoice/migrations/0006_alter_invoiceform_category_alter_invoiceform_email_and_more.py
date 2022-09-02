# Generated by Django 4.1 on 2022-09-02 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0005_remove_invoiceform_fname_remove_invoiceform_lname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoiceform',
            name='category',
            field=models.TextField(choices=[('grocery', 'GROCERY'), ('electronics', 'ELECTRONICS')], max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='invoiceform',
            name='email',
            field=models.EmailField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='invoiceform',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]