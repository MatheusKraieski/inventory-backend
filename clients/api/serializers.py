from rest_framework import serializers
from clients import models

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Clients
        fields = '__all__'