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
                favorite=request.data.get('favorite'),
            )
            return {'Product created successfully.'}, 201
        except Exception as e:
            print(e)
            return {'Product could not be created.'}, 400

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
        
        return product_dic, 200

    
    def update_product(self, product, request):
        product.name = request.data.get("name", product.name)
        product.category_id = request.data.get("category_id", product.category)
        product.cost = request.data.get("cost", product.cost)
        product.inventory_number = request.data.get("inventory_number", product.inventory_number)
        product.minimum_amount = request.data.get("minimum_amount", product.minimum_amount)
        product.favorite = request.data.get("favorite", product.favorite)

        product.save()   
        return product, 200

    def build_product_dict(self, product):
        product_dict = {
            "name": product.name,
            "category_id": product.category_id,
            "cost": product.cost,
            "inventory_number": product.inventory_number,
            "favorite":product.favorite,
            "minimum_amount":product.minimum_amount,
            "images": product.images.values(),
        }         
        return product_dict, 200