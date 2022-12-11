from rest_framework import viewsets
from cart.api import serializers
from cart import models
#
# class LineItemViewSet(viewsets.ModelViewSet):
#     serializer_class = serializers.LineItemSerializer
#     queryset = models.LineItem.objects.all()