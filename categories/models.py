from django.db import models
from mptt.models import TreeForeignKey


# Create your models here.
class Categories(models.Model):
    name = models.CharField('nome', max_length=100, unique=True)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        verbose_name='categoria',
    )
