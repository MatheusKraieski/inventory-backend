from apps.products.models import Product, ProductImage
from distutils.util import strtobool
from apps.categories.models import Category
from django.db import transaction


class ProductSerializer:
    def create_product(self, request):
        try:
            with transaction.atomic():
                product = Product.objects.create(
                    name=request.data.get('name'),
                    category_id=request.data.get("category_id"),
                    cost=request.data.get('cost'),
                    inventory_number=request.data.get('inventory_number'),
                    favorite=eval(request.data.get('favorite').capitalize()),
                )

                self.add_images_to_product(product, request.data.getlist('images'))

            return {"detail": "Product created successfully."}, 201
        except Exception as e:
            print(e)
            return {"error": "'Product could not be created."}, 400

    def get_product(self, product):
        product_dict = self.build_product_dict(product)
        return product_dict, 200

    def update_product(self, product, request):
        try:
            with transaction.atomic():
                category = Category.objects.get(pk=int(request.data.get("category_id", product.category.pk)))
                product.name = request.data.get("name", product.name)
                product.category = category
                product.cost = float(request.data.get("cost", product.cost))
                product.inventory_number = float(request.data.get("inventory_number", product.inventory_number))
                product.favorite = bool(strtobool(request.data.get('favorite', "false").capitalize()))
                if request.data:
                    images = request.data.getlist("images")
                    if images:
                        product.images.all().delete()
                        self.add_images_to_product(product, images)

                product.save()
                return {"detail": "Product was updated successfully."}, 201
        except Exception as e:
            print(e)
            return {"error": "Product could not be changed."}, 400

    @staticmethod
    def build_product_dict(product):
        category = product.category.get_root()
        product_dict = {
            "id": product.pk,
            "name": product.name,
            "category_id": product.category_id,
            "cost": product.cost,
            "inventory_number": product.inventory_number,
            "favorite": product.favorite,
            "image": product.images.values(),
            "category": {
                "id": category.pk,
                "name": category.name,
            }
        }
        return product_dict

    def get_all_products_dict(self, products):
        product_list_dict = []

        for product in products:
            product_dict = self.build_product_dict(product)
            product_list_dict.append(product_dict)

        return product_list_dict, 200

    @staticmethod
    def add_images_to_product(product, images):
        for image in images:
            ProductImage.objects.create(
                product=product,
                image=image,
            )
