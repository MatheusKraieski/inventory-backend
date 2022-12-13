from rest_framework import serializers
from apps.line_items import models


class LineItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LineItem
        fields = '__all__'
