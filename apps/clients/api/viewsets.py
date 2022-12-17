from rest_framework import viewsets
from apps.clients.api import serializers
from apps.clients import models
from apps.clients.models import Client
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.line_items.api.serializers import LineItemSerializer


class ClientList(APIView):
    def get(self, request):
        clients = Client.objects.values()
        return Response(clients, 200)

    def post(self, request):    
        serializer = LineItemSerializer()
           
        response, status = serializer.add_item(request)
        return Response(response, status)

    