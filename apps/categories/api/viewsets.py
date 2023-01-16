from rest_framework import viewsets
from apps.categories.api import serializers
from apps.categories.models import Category
from apps.categories.api.serializers import NewCategory, CategoriesSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class CategoryView(APIView):
    serializer = NewCategory()
    def get(self, request):
        categories = Category.objects.all()     

        response, status = self.serializer.get_all_categories_dict(categories)
        return Response(response, status)

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

    def delete(self, request, category_pk):
        product = get_object_or_404(Category, pk=category_pk)
        response, status = self.serializer.delete_category(product)
        return Response(response, status)