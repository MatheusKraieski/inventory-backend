from rest_framework import serializers
from apps.categories import models


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'
