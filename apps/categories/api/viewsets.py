from rest_framework import viewsets
from apps.categories.api import serializers
from apps.categories.models import Category
from apps.categories.api.serializers import NewCategory
from rest_framework.views import APIView
from rest_framework.response import Response

class CategoryView(APIView):
    def get(self, request):
        categories = Category.objects.values()
        return Response(categories, 200)

    def post(self, request):    
        serializer = NewCategory()
            
        response, status = serializer.create_category(request)
        return Response(response, status)    