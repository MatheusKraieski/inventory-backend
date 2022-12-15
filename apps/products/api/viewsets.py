from apps.products.models import Product
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.products.api.serializers import ProductSerializer





class ProductList(APIView):
    def get(self, request):
        products = Product.objects.values()
        return Response(products, 200)


@api_view(['POST'])
def create_product(request):
    serializer = ProductSerializer()
    
    response, status = serializer.full_validation(request)
    if status != 200:
        return Response(response, status)
    
    response, status = serializer.create_product(request)
    return Response(response, status)        
