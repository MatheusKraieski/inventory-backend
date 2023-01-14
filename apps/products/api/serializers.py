from apps.products.models import Product, ProductImage
from distutils.util import strtobool
from apps.categories.models import  Category


class ProductImageSerializer:
    class Meta:
        model = ProductImage
        fields = '__all__'

class ProductSerializer:
    def create_product(self, request):
        try:
            product = Product.objects.create(
                name=request.data.get('name'),
                category_id=request.data.get("category_id"),
                cost=request.data.get('cost'),
                inventory_number=request.data.get('inventory_number'),
                favorite=eval(request.data.get('favorite').capitalize()),
            )

            self.add_images_to_product(product, request.data.getlist('images'))


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
            "image":product.images.values(),
        }

        return product_dic, 200


    def update_product(self, product, request):
        try:
            category = Category.objects.get(pk=int(request.data.get("category_id", product.category.pk)))
            product.name = request.data.get("name", product.name)
            product.category = category
            product.cost = float(request.data.get("cost", product.cost))
            product.inventory_number = float(request.data.get("inventory_number", product.inventory_number))
            product.favorite = bool(strtobool(request.data.get('favorite', "false").capitalize()))
            product.images.all().delete()

            self.add_images_to_product(product, request.data.getlist("images"))

            product.save()
            return product, 200
        except Exception as e:
            print(e)
            return {'Product could not be changed.'}, 400


    def build_product_dict(self, product):
        product_dict = {
            "id": product.pk,
            "name": product.name,
            "category_id": product.category_id,
            "cost": product.cost,
            "inventory_number": product.inventory_number,
            "favorite":product.favorite,
            "image":product.images.values(),
        }
        return product_dict, 200

    def get_all_products_dict(self, products):
        product_list_dict = []

        for product in products:
            product_dict, status = self.build_product_dict(product)
            product_list_dict.append(product_dict)

        return product_list_dict, 200

    @staticmethod
    def add_images_to_product(product, images):
        for image in images:
            ProductImage.objects.create(
                product=product,
                image=image,
            )