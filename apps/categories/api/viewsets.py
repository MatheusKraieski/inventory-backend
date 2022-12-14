from rest_framework import viewsets
from apps.categories.api import serializers
from apps.categories.models import Category
from rest_framework.views import APIView
from rest_framework.response import Response

class CategoryView(APIView):
    def get(self, request):
        categories = Category.objects.values()
        return Response(categories, 200)