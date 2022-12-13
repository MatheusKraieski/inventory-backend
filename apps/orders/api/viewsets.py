from apps.orders.models import Order
from rest_framework.response import Response
from rest_framework.views import APIView

class Orders(APIView):
    def get(self, request):
        orders = Order.objects.values()
        return Response(orders, 200)