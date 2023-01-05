from apps.products.models import Product, ProductImage
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.products.api.serializers import ProductSerializer, ProductImageSerializer
from rest_framework.parsers import MultiPartParser

@api_view(['GET'])
def search_products(request):
    if request.GET.get('q'):
        products = Product.objects\
            .filter(search_field__icontains=request.GET.get('q'))
    else:
        products = Product.objects\
            .filter()
        serializer = ProductSerializer(products, many=True)
    return Response(products)

class ProductList(APIView):
    parser_classes = (MultiPartParser,) 
    def get(self, request):
        products = Product.objects.values()
        return Response(products, 200)     

    def post(self, request):    
        serializer = ProductSerializer()
           
        response, status = serializer.create_product(request)
        return Response(response, status)
       


class ProductDetail(APIView):
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
   