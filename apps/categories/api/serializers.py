from rest_framework import serializers
from apps.categories import models
from apps.categories.models import Category


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class NewCategory:
    def create_category(self, request):
        try:
            category = Category.objects.create(
                name=request.data.get('name'),
                parent=request.data.get("parent"),
            )

            return {'Category created successfully.'}, 201
        except Exception as e:
            print(e)
            return {'Product could not be created.'}, 400