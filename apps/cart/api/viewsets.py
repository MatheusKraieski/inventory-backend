from rest_framework import viewsets
from apps.cart.api import serializers
from apps.cart import models
#
# class CartViewSet(viewsets.ModelViewSet):
#     serializer_class = serializers.CartSerializer
#     queryset = models.Cart.objects.all()