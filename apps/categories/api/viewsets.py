from rest_framework import viewsets
from apps.categories.api import serializers
from apps.categories.models import Category
from apps.categories.api.serializers import NewCategory, CategoriesSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from django.shortcuts import get_object_or_404

class CategoryView(APIView):
    def get(self, request):
        categories = Category.objects.values()
        return Response(categories, 200)

    def post(self, request):    
        serializer = NewCategory()
            
        response, status = serializer.create_category(request)
        return Response(response, status)
    
class CategoryDetail(APIView):
    serializer = NewCategory()

    def put(self, request, category_pk):
        category = get_object_or_404(Category, pk=category_pk)
        response, status = self.serializer.update_category(category, request)
        return Response(response, status)

    def get(self, request, category_pk):
            category = get_object_or_404(Category, pk=category_pk)
            response, status = self.serializer.get_category(category)
            return Response(response, status)