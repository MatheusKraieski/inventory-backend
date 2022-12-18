from apps.line_items.api.serializers import LineItemSerializer


class CartSerializer:
    line_item_serializer = LineItemSerializer()

    def get_cart_dict(self, cart):
        context = {
            "cart": {
                "id": cart.id,
                "line_items": self.line_item_serializer.get_line_items_dict(cart.line_items.all())
            }
        }
        return context, 200
