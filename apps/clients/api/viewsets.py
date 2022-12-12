from rest_framework import viewsets
from apps.clients.api import serializers
from apps.clients import models

class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ClientSerializer
    queryset = models.Client.objects.all()