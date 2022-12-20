from django.db import models
from apps.cart.models import Cart
from apps.orders.models import Order
from apps.products.models import Product


class LineItem(models.Model):
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, blank=True, related_name='line_items')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True, related_name='line_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def total_price(self):
        return self.price * self.quantity
    
    def __str__(self):
        return self.product.name
