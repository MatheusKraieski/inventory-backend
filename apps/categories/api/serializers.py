from rest_framework import serializers
from apps.categories import models
from apps.categories.models import Category
from django.db import transaction


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class NewCategory:
    @staticmethod
    def create_category(request):
        try:
            Category.objects.create(
                name=request.data.get('name'),
                parent_id=request.data.get("parent_id")
            )

            return {'Category created successfully.'}, 201
        except Exception as e:
            print(e)
            return {'Product could not be created.'}, 400

    @staticmethod
    def update_category(category, request):
        try:
            category.name = request.data.get("name", category.name)
            category.save()
            return {"detail": "Category was updated successfully."}, 201
        except Exception as e:
            print(e)
            return {"error": "Category could not be changed."}, 400

    def get_category(self, category):
        category_dict = self.build_category_dict(category)
        return category_dict, 200        

    def build_category_dict(self, category):
        product_categories = category.get_ancestors(include_self=True).reverse()
        category_dict = {
            "id": category.pk,
            "name": category.name,
            # "parent": product_categories
        }
        return category_dict

    def get_all_categories_dict(self, categories):
        category_list_dict = []

        for category in categories:
            category_dict = self.build_category_dict(category)
            category_list_dict.append(category_dict)

        return category_list_dict, 200    
        
    def get_subcategories(self, category: Category, category_dict):
        if category.get_ancestors():
            parent_category = category.parent
            category_dict["category"] = self.build_category_dict(parent_category)
            if parent_category.get_ancestors():
                category_dict["category"] = self.get_subcategories(parent_category, category_dict.get("category"))
        return category_dict

    def delete_category(self, category):
        try:
            category.delete()
            return {"detail": "Product was deleted successfully"}, 201
        except Exception as err:
            print(err)
            return {"error": "Product could not be deleted"}, 400
