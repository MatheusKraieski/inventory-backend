import uuid

from django.db import models
from apps.clients.models import Client


class Order(models.Model):
    PAYMENT_TYPE_CHOICES = (
        (1, 'Boleto'),
        (2, 'Cartão de crédito'),
        (3, 'Cartão de débito'),
        (4, 'Pix'),
    )

    PAYMENT_STATUS = (
        (0, 'Pagamento não finalizado'),
        (1, 'Pagamento autorizado'),
        (2, 'Pagamento confirmado'),
        (3, 'Pagamento negado'),
        (10, 'Pagamento cancelado'),
        (11, 'Devolvido'),
        (12, 'Pendente'),
        (13, 'Abortado'),
        (20, 'Agendado'),
        (21, 'Enviado'),
        (22, 'Recebido'),
    )

    ORDER_STATUS = (
        (0, 'Pagamento não finalizado'),
        (1, 'Pagamento autorizado'),
        (2, 'Pagamento confirmado'),
        (3, 'Pagamento negado'),
        (10, 'Pagamento cancelado'),
        (11, 'Devolvido'),
        (12, 'Pendente'),
        (13, 'Abortado'),
        (20, 'Agendado'),
        (21, 'Enviado'),
        (22, 'Recebido'),
        (30, 'Gerando nota fiscal'),
        (31, 'Enviado'),
        (32, 'Entregue'),
    )

    FRETE_TYPE = (
        (1, 'PAC'),
        (2, 'SEDEX'),
    )

    ref = models.CharField(max_length=255, null=True, blank=True)
    order_status = models.IntegerField('Status do pedido', choices=ORDER_STATUS, default=12)
    payment_type = models.IntegerField('Tipo', choices=PAYMENT_TYPE_CHOICES, default=1)
    receipt = models.FileField('Nota Fiscal', upload_to='uploads/receipts', max_length=100, null=True, blank=True)
    total_amount_products = models.DecimalField('Total produtos', decimal_places=2, max_digits=12)
    total_amount_discount = models.DecimalField('Total desconto', decimal_places=2, max_digits=12)
    total_amount = models.DecimalField('Total', decimal_places=2, max_digits=12)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='orders', verbose_name='cliente')

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return str(self.uuid)

    def save(self, *args, **kwargs):
        self.ref = self.generate_ref()
        super(Order, self).save(*args, **kwargs)

    @staticmethod
    def generate_ref():
        ref = uuid.uuid4().hex[:10].upper()
        while Order.objects.filter(ref=ref).exists():
            ref = uuid.uuid4().hex[:10].upper()
        return ref

    def add_line_items_to_order(self, cart):
        try:
            for line_item in cart.line_items.all():
                line_item.order_id = self.pk
                line_item.cart_id = ''
                line_item.save()
            return [], 200
        except Exception as err:
            return {'error': err}, 400

    @staticmethod
    def update_stock(cart):
        try:
            for line_item in cart.line_items.all():
                line_item.product.stock_quantity = line_item.product.stock_quantity - line_item.quantity
                line_item.product.save()
            return [], 200
        except Exception as e:
            print(e)
            return {'detail': 'Quantidade de items é maior que a quantidade no stock.'}, 400
