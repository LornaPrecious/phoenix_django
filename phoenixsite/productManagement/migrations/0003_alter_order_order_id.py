# Generated by Django 4.2 on 2023-08-29 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productManagement', '0002_alter_order_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True),
        ),
    ]