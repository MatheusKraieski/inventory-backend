from apps.orders.models import Order


class OrderSerializer:
    def get_orders(self):
        orders = Order.objects.all()
        context = []
        for order in orders:
            order_dict = {
                "ref": order.ref,
                "payment_type": order.payment_type,
                "line_items": order.line_items.values()
            }
            context.append(order_dict)
        return context, 200

    def create_order(self, request, cart):
        try:
            order = Order.objects.create(
                ref=request.data.get("ref"),
                payment_type=request.data.get("payment_type"),
                client_id=request.data.get("client_id")
            )
            order.add_line_items_to_order(cart)
            return "Order created successfully.", 200
        except Exception as err:
            print(err)
            return 'order nao pode ser criada', 400
