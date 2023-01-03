from apps.products.models import Product, ProductImage


class ProductImageSerializer:
    class Meta:
        model = ProductImage
        fields = '__all__'

class ProductSerializer:
    def create_product(self, request):
        try:
            Product.objects.create(
                name=request.data.get('name'),
                category_id=request.data.get("category_id"),
                cost=request.data.get('cost'),
                inventory_number=request.data.get('inventory_number'),
                minimum_amount=request.data.get('minimum_amount'),
                image_product=request.data.get('image_product'),
                favorite=request.data.get('favorite'),
            )
            return {'detail': 'Product created successfully.'}, 201
        except Exception as e:
            print(e)
            return {'detail': 'Product could not be created.'}, 400

    def get_product(self, product_pk):
        product = Product.objects.get(pk=product_pk)
        product_dic = {
                "name": product.name,
                "category": product.category_id,
                "cost": product.cost,
                "inventory_number": product.inventory_number,
                "favorite":product.favorite,
                "images": product.images.values(),
            } 
        
        return {"detail": product_dic}, 200
