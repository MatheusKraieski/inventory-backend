from django.db import models


class Cart(models.Model):
    FRETE_TYPE = (
        (1, 'Pac'),
        (2, 'Sedex')
    )
    has_frete = models.BooleanField(default=False)
    pac_value = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    pac_prazo = models.IntegerField(null=True, blank=True)
    sedex_value = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    sedex_prazo = models.IntegerField(null=True, blank=True)
    frete_type = models.IntegerField(choices=FRETE_TYPE, default=1)

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
