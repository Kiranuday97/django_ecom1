# Generated by Django 4.1.7 on 2023-03-07 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_addproduct_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addproduct',
            name='description',
            field=models.TextField(),
        ),
    ]
