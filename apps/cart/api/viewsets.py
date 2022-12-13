from rest_framework.response import Response
from rest_framework.views import APIView
from apps.cart.models import Cart
from apps.products.models import Product
from apps.line_items.models import LineItem
from apps.cart.api.serializers import CartSerializer


class GetCurrentCart(APIView):
    def post(self, request):
        try:
            cart = Cart.objects.get(pk=request.data.get('cart_id'))
        except:
            cart = Cart.objects.create()
        serializer = CartSerializer(cart, context={'request': request})
        return Response(serializer.data, 200)


class AddLineItemToCart(APIView):
    def post(self, request):
        cart = Cart.objects.get(pk=request.data.get('cart_id'))
        request.data['product'] = Product.objects.get(pk=request.data.get('product_id'))
        if request.data.get('product').inventory_number == 0:
            return Response({'detail': 'Product out of stock.'}), 400

        quantity = request.data.get("quantity")
        try:
            line_item = LineItem.objects.get(product_id=request.data.get('product'), cart=cart)
            line_item.quantity = quantity
            line_item.save()
        except:
            LineItem.objects.create(product=request.data.get('product'), quantity=quantity, cart=cart)
        serializer = CartSerializer(cart, context={'request': request})
        return Response({"cart": serializer.data}, 200)
