from rest_framework.response import Response
from rest_framework.views import APIView
from apps.cart.models import Cart
from apps.cart.api.serializers import CartSerializer
from apps.line_items.models import LineItem
from apps.products.models import Product


class GetCurrentCart(APIView):
    cart_serializer = CartSerializer()

    def get(self, request, cart_id):
        cart = Cart.objects.get(pk=cart_id)
        response, status = self.cart_serializer.get_cart_dict(cart)
        return Response(response, status)


class AddLineItemToCart(APIView):
    cart_serializer = CartSerializer()

    def post(self, request):
        cart = Cart.objects.get(pk=request.data.get('cart_id'))

        product = Product.objects.get(pk=request.data.get('product_id'))
        if product.inventory_number == 0:
            return Response({'detail': 'Product out of stock.'}), 400

        quantity = request.data.get("quantity")
        try:
            line_item = LineItem.objects.get(product=product, cart=cart)
            line_item.quantity = quantity
            line_item.save()
        except LineItem.DoesNotExist:
            LineItem.objects.create(product=product, quantity=quantity, cart=cart)

        response, status = self.cart_serializer.get_cart_dict(cart)
        return Response(response, status)


class UpdateLineItemQuantity(APIView):
    def put(self, request, line_item_uuid):
        line_item = LineItem.objects.get(pk=request.data.get('line_item_id'))
        if request.data.get('type') == 'update':
            line_item.quantity = int(request.data.get('quantity'))
        elif request.data.get('type') == 'increase':
            line_item.quantity += 1
        elif request.data.get('type') == 'decrease':
            if line_item.quantity > 1:
                line_item.quantity -= 1
