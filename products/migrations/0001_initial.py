# Generated by Django 4.1.3 on 2022-12-04 03:40

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, default=100, max_digits=12)),
                ('category', models.CharField(max_length=255)),
                ('cost', models.DecimalField(decimal_places=2, default=100, max_digits=12)),
                ('promotion_price', models.DecimalField(decimal_places=2, default=100, max_digits=12)),
                ('inventory_number', models.DecimalField(decimal_places=2, default=100, max_digits=12)),
                ('minimum_amount', models.DecimalField(decimal_places=2, default=100, max_digits=12)),
                ('image_product', models.ImageField(blank=True, null=True, upload_to=products.models.upload_image_product)),
                ('favorite', models.BooleanField(default=False)),
            ],
        ),
    ]
