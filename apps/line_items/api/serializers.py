from rest_framework import serializers
from apps.line_items.models import LineItem


class LineItemSerializer(serializers.ModelSerializer):
    def add_item(self, request):
        try:
            LineItem.objects.create(
                quantity=request.data.get('Quantity'),
                cart=request.data.get('cart'),
                order=request.data.get("order"),
                product=request.data.get('product'),
            )
            return {'detail': 'item adicionado.'}, 201
        except Exception as e:
            print(e)
            return {'detail': 'item não pode ser adicionado.'}, 400    