# Generated by Django 4.1.3 on 2022-12-16 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='promotion_price',
        ),
    ]