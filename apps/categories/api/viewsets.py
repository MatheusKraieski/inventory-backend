from rest_framework import viewsets
from apps.categories.api import serializers
from apps.categories import models


class CategoriesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CategoriesSerializer
    queryset = models.Categories.objects.all()