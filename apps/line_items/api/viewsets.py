from rest_framework import viewsets
from apps.line_items.models import LineItem
from apps.line_items.api.serializers import LineItemSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class ClientList(APIView):
    def get(self, request):
        line_tem = LineItem.objects.values()
        return Response(line_tem, 200)

    def post(self, request):    
        serializer = LineItemSerializer()
           
        response, status = serializer.add_client(request)
        return Response(response, status)
