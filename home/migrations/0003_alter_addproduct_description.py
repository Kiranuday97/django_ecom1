# Generated by Django 4.1.7 on 2023-03-07 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_order_cart_product_cart_quantity_alter_cart_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addproduct',
            name='description',
            field=models.TextField(max_length=2000),
        ),
    ]
