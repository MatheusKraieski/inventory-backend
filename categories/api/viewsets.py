from rest_framework import viewsets
from categories.api import serializers
from categories import models

class CategoriesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CategoriesSerializer
    queryset = models.Categories.objects.all()