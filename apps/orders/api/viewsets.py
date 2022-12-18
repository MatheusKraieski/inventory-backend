from apps.orders.models import Order
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.orders.api.serializers import OrderSerializer


class Orders(APIView):
    def get(self, request):
        orders = Order.objects.values()
        return Response(orders, 200)

    def post(self, request):
        serializer = OrderSerializer()
        message, status = serializer.create_order(request)
        return Response(message, status)
