from django.db import models
from apps.cart.models import Cart
from apps.orders.models import Order
from apps.products.models import Product


class LineItem(models.Model):
    quantity = models.IntegerField(default=1)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, blank=True, related_name='line_items')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True, related_name='line_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def total_price(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return self.product.name
