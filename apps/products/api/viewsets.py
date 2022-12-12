from rest_framework import viewsets
from apps.products.api import serializers
from apps.products import models


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()
