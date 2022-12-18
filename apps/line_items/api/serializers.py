from rest_framework import serializers
from apps.line_items.models import LineItem


class LineItemSerializer():
    def get_line_item (self):
        line_items = LineItem.objects.all()
        context = []
        for line_item in line_items:
            line_item_dict = {
                "quantity": line_item.quantity,
                "cart": line_item.cart,
                "order": line_item.order,
                "product": line_item.product.values()
            }
            context.append(line_item_dict)
        return context, 200

    class Meta:
        model = LineItem
        fields = ['id', 'quantity', 'product', 'total_price']

    def get_total_price(self, obj: LineItem):
        return obj.total_price()
