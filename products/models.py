from django.db import models
from uuid import uuid4


# Create your models here.
def upload_image_product(self, filename):
    return f"{self.pk}-{filename}"


class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=12, default=100)
    category = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=12, decimal_places=2, default=100)
    promotion_price = models.DecimalField(max_digits=12, decimal_places=2, default=100)
    inventory_number = models.DecimalField(decimal_places=2, max_digits=12, default=100)
    minimum_amount = models.DecimalField(decimal_places=2, max_digits=12, default=100)
    image_product = models.ImageField(max_length=100, null=True, blank=True, upload_to=upload_image_product)
    favorite = models.BooleanField(default=False)
