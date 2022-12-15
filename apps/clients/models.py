from django.db import models
from uuid import uuid4


class Client(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField('Nome', max_length=100)
    email = models.EmailField('E-Mail', max_length=100, unique=True)
    cpf = models.CharField('CPF', blank=True, null=True, max_length=11, unique=True)
    cnpj = models.CharField('CNPJ', blank=True, null=True, max_length=14, unique=True)
    first_phone = models.CharField('Telefone', max_length=50, null=True, blank=True)
    second_phone = models.CharField('Telefone 2', max_length=50, null=True, blank=True)


    def __str__(self):
        return self.name