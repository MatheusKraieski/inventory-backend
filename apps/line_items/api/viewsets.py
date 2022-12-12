from rest_framework import viewsets
from apps.cart import models
from apps.cart.api import serializers
#
# class LineItemViewSet(viewsets.ModelViewSet):
#     serializer_class = serializers.LineItemSerializer
#     queryset = models.LineItem.objects.all()