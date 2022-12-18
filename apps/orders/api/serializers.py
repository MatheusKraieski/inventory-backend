from apps.orders.models import Order


class OrderSerializer:
    def create_order(self, request):
        try:
            Order.objects.create(
                ref=request.data.get("ref"),
                payment_type=request.data.get("payment_type"),
                client_id=request.data.get("client_id")
            )
            return "Order created successfully.", 200
        except Exception as err:
            print(err)
            return 'order nao pode ser criada', 400
