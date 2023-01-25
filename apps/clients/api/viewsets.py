from apps.clients.models import Client
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.clients.api.serializers import ClientSerializer
from django.shortcuts import get_object_or_404
from rest_framework.parsers import MultiPartParser


class ClientList(APIView):
    def get(self, request):
        clients = Client.objects.values()
        return Response(clients, 200)

    def post(self, request):    
        serializer = ClientSerializer()
           
        response, status = serializer.add_client(request)
        return Response(response, status)


class ClientDetail(APIView):
    parser_classes = (MultiPartParser,)
    serializer = ClientSerializer()
 
    def put(self, request, client_pk):
        client = get_object_or_404(Client, pk=client_pk)
        response, status = self.serializer.update_client(client, request)
        return Response(response, status)

    def get(self, request, client_pk):
        client = get_object_or_404(Client, pk=client_pk)
        response, status = self.serializer.get_client(client)
        return Response(response, status)

    def delete(self, request, client_pk):
        client = get_object_or_404(Client, pk=client_pk)
        response, status = self.serializer.delete_client(client)
        return Response(response, status)


    