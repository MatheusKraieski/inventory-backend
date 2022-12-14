from django.db import models
from mptt.models import TreeForeignKey
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.
class Category(models.Model):
    name = models.CharField('nome', max_length=100, unique=True)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        verbose_name='categoria',
    )

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
