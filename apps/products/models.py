from django.db import models
from apps.categories.models import Category


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=12,)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    cost = models.DecimalField(max_digits=12, decimal_places=2,)
    promotion_price = models.DecimalField(max_digits=12, decimal_places=2)
    inventory_number = models.DecimalField(decimal_places=2, max_digits=12)
    minimum_amount = models.DecimalField(decimal_places=2, max_digits=12)
    image_product = models.ImageField(max_length=100, null=True, blank=True, upload_to="uploads/products")
    favorite = models.BooleanField(default=False)