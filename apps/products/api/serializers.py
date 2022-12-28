from apps.products.models import Product


class ProductSerializer:
    def create_product(self, request):
        try:
            Product.objects.create(
                name=request.data.get('name'),
                price=request.data.get('price'),
                category_id=request.data.get("category_id"),
                cost=request.data.get('cost'),
                promotion_price=request.data.get('promotion_price'),
                inventory_number=request.data.get('inventory_number'),
                minimum_amount=request.data.get('minimum_amount'),
                image_product=request.data.get('image_product'),
                favorite=request.data.get('favorite'),
            )
            return {'detail': 'Product created successfully.'}, 201
        except Exception as e:
            print(e)
            return {'detail': 'Product could not be created.'}, 400

    def get_product(self, request, product_pk):
        product = Product.objects.get(pk=product_pk)
        product_dic = {
                "name": product.name,
                "price": product.price,
                "category_id": product.category_id,
                "cost": product.cost,
                "promotion_price": product.promotion_price,
                "inventory_number": product.inventory_number,
                "image_product": product.image_product,
                "favorite":product.favorite,
        }
        return {"detail": product_dic}, 200
