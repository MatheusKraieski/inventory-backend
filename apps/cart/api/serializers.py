from rest_framework import serializers
from apps.cart import models
from apps.line_items.api.serializers import LineItemSerializer


class CartSerializer(serializers.ModelSerializer):
    line_items = LineItemSerializer(many=True, read_only=True)

    class Meta:
        model = models.Cart
        fields = ['id', 'line_items']
