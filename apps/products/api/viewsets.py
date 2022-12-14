from apps.products.models import Product
from rest_framework.views import APIView
from rest_framework.response import Response


class ProductList(APIView):
    def get(self, request):
        products = Product.objects.values()
        return Response(products, 200)
