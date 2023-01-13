from apps.products.models import Product, ProductImage
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.products.api.serializers import ProductSerializer, ProductImageSerializer
from rest_framework.parsers import MultiPartParser

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
    
    def get(self, request, product_pk):
        serializer = ProductSerializer()
        
        response, status = serializer.get_product(product_pk)
        return Response(response, status)

    def put(self, request, product_pk):
        product = Product.objects.get(pk=product_pk)
        serializer = ProductSerializer()
        
        response, status = serializer.update_product(product, request)
        if status != 200:
            return Response(response, status)

        response, status = serializer.build_product_dict(response)
        return Response(response, status)
