# Generated by Django 4.1.3 on 2023-01-09 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_category_product_category_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category_id',
            new_name='category',
        ),
    ]
