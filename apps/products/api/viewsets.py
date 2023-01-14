from apps.products.models import Product
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.products.api.serializers import ProductSerializer
from rest_framework.parsers import MultiPartParser
from django.shortcuts import get_object_or_404


class ProductList(APIView):
    serializer = ProductSerializer()
    parser_classes = (MultiPartParser,)

    def get(self, request):
        if request.GET.get('q'):
            products = Product.objects.filter(search_text=request.GET.get('q'))
        else:
            products = Product.objects.all()

        response, status = self.serializer.get_all_products_dict(products)   
        return Response(response, status)

    def post(self, request):    
                   
        response, status = self.serializer.create_product(request)
        return Response(response, status)


class ProductDetail(APIView):
    parser_classes = (MultiPartParser,)
    serializer = ProductSerializer()
    
    def get(self, request, product_pk):
        product = get_object_or_404(Product, pk=product_pk)
        response, status = self.serializer.get_product(product)
        return Response(response, status)

    def put(self, request, product_pk):
        product = get_object_or_404(Product, pk=product_pk)
        response, status = self.serializer.update_product(product, request)
        return Response(response, status)
