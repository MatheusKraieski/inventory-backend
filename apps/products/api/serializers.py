from rest_framework import serializers
from apps.products import models
from apps.products.models import Product

class ProductSerializer:
    
    def create_product(self, request):
        try:
            Product.objects.create(
                name=request.data.get('name'),
                price=request.data.get('price'),
                category=request.data.get('category'),
                cost=request.data.get('cost'),
                promotion_price=request.data.get('promotion_price'),
                inventory_number=request.data.get('inventory_number'),
                minimum_amount=request.data.get('minimum_amount'),
                image_product=request.data.get('image_product'),
                favorite=request.data.get('favorite'),
            )
            return {'detail': 'produto criado com sucesso.'}, 201
        except Exception as e:
            print(e)
            return {'detail': 'produto não pode ser criado.'}, 400    