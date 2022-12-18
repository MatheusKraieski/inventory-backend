from apps.orders.models import Order
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.orders.api.serializers import OrderSerializer
from apps.cart.models import Cart


class Orders(APIView):
    order_serializer = OrderSerializer()

    def get(self, request):
        orders = Order.objects.all()
        response, status = self.order_serializer.get_orders_dict(orders)
        return Response(response, status)

    def post(self, request):
        cart = Cart.objects.get(pk=request.data.get('cart_id'))
        message, status = self.order_serializer.create_order(request, cart)
        return Response(message, status)
