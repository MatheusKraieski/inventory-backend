from django.db import models
from apps.categories.models import Category


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    cost = models.DecimalField(max_digits=12, decimal_places=2,)
    inventory_number = models.DecimalField(decimal_places=2, max_digits=12)
    minimum_amount = models.DecimalField(decimal_places=2, max_digits=12)
    favorite = models.BooleanField(default=False)
    search_field = models.TextField('Pesquisar', null=True, blank=True)


    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', verbose_name='produto')
    image = models.ImageField('Imagem', upload_to='uploads/produtos', max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Imagem'
        verbose_name_plural = 'Imagens'

    def __str__(self):
        return 'imagem'
        