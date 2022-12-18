from rest_framework import serializers
from apps.line_items.models import LineItem


class LineItemSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = LineItem
        fields = ['id', 'quantity', 'product', 'total_price']

    def get_total_price(self, obj: LineItem):
        return obj.total_price()
