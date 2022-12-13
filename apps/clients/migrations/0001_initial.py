# Generated by Django 4.1.3 on 2022-12-12 22:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='E-Mail')),
                ('cpf', models.CharField(blank=True, max_length=11, null=True, unique=True, verbose_name='CPF')),
                ('cnpj', models.CharField(blank=True, max_length=14, null=True, unique=True, verbose_name='CNPJ')),
                ('first_phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='Telefone')),
                ('second_phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='Telefone 2')),
            ],
        ),
    ]
