from rest_framework import serializers
from apps.orders import models

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = '__all__'