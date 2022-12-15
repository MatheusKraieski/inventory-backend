# Generated by Django 4.1.3 on 2022-12-15 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_frete', models.BooleanField(default=False)),
                ('pac_value', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('pac_prazo', models.IntegerField(blank=True, null=True)),
                ('sedex_value', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('sedex_prazo', models.IntegerField(blank=True, null=True)),
                ('frete_type', models.IntegerField(choices=[(1, 'Pac'), (2, 'Sedex')], default=1)),
            ],
            options={
                'verbose_name': 'Carrinho',
                'verbose_name_plural': 'Carrinhos',
            },
        ),
    ]
