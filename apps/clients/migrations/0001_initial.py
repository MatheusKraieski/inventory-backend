# Generated by Django 4.1.3 on 2022-12-18 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='E-Mail')),
                ('cpf', models.CharField(blank=True, max_length=11, null=True, unique=True, verbose_name='CPF')),
                ('cnpj', models.CharField(blank=True, max_length=14, null=True, unique=True, verbose_name='CNPJ')),
                ('first_phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='Telefone')),
                ('second_phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='Telefone 2')),
            ],
        ),
    ]
