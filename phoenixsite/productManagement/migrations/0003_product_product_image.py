# Generated by Django 4.2 on 2023-08-09 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productManagement', '0002_remove_order_order_discount_remove_order_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]