from rest_framework import serializers
from products import models

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Products
        fields = '__all__'