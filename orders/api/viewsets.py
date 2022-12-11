from rest_framework import viewsets
from orders.api import serializers
from orders import models
#
# class LineItemViewSet(viewsets.ModelViewSet):
#     serializer_class = serializers.LineItemSerializer
#     queryset = models.LineItem.objects.all()