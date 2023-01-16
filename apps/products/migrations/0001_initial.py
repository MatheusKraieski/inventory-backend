# Generated by Django 4.1.3 on 2023-01-16 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=12)),
                ('inventory_number', models.DecimalField(decimal_places=2, max_digits=12)),
                ('favorite', models.BooleanField(default=False)),
                ('search_field', models.TextField(blank=True, null=True, verbose_name='Pesquisar')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='categories.category')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/produtos', verbose_name='Imagem')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='products.product', verbose_name='produto')),
            ],
            options={
                'verbose_name': 'image',
                'verbose_name_plural': 'Imagens',
            },
        ),
    ]
