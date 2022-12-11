from rest_framework import viewsets
from cart.api import serializers
from cart import models
#
# class CartViewSet(viewsets.ModelViewSet):
#     serializer_class = serializers.CartSerializer
#     queryset = models.Cart.objects.all()