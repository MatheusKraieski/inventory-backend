from django.db import models


class Cart(models.Model):
    PAYMENT_TYPE = (
        (1, 'Pix'),
        (2, 'Cartão de Débito'),
        (3, 'Cartão de Crédito'),
        (4, 'Dinheiro')
    )

    
    payment_type = models.IntegerField(choices=PAYMENT_TYPE, default=1, null=False)

    class Meta:
        verbose_name = 'Carrinho'
        verbose_name_plural = 'Carrinhos'

    def frete_price(self):
        if self.has_frete:
            return self.pac_value if self.frete_type == 1 else self.sedex_value
        else:
            return 0

    def line_items_quantity(self):
        return sum([line_item.quantity for line_item in self.line_items.all()])

    def total_products(self):
        return sum([line_item.total_products() for line_item in self.line_items.all()])
    
