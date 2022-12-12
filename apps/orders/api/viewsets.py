from rest_framework import viewsets
from apps.orders.api import serializers
from apps.orders import models
#
# class LineItemViewSet(viewsets.ModelViewSet):
#     serializer_class = serializers.LineItemSerializer
#     queryset = models.LineItem.objects.all()