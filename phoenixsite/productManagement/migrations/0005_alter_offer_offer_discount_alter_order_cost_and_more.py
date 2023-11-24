# Generated by Django 4.2 on 2023-11-24 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productManagement', '0004_alter_orderitem_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='offer_discount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='paymentinfo',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_tax',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='delivery_cost',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
