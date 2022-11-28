from rest_framework import viewsets
from clients.api import serializers
from clients import models

class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ClientSerializer
    queryset = models.Clients.objects.all()