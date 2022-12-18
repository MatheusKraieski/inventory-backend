from typing import List
from apps.line_items.models import LineItem


class LineItemSerializer:
    def get_line_items_dict(self, line_items: List[LineItem]):
        line_items_dict = []
        for line_item in line_items:
            line_item_dict = {
                "id": line_item.id,
                "quantity": line_item.quantity,
                "total_price": line_item.total_price(),
                "product": {
                    "id": line_item.product.id,
                    "name": line_item.product.name,
                    "price": line_item.product.price,
                    "cost": line_item.product.cost,
                    "inventory_number": line_item.product.inventory_number,
                    "minimum_amount": line_item.product.minimum_amount,
                    "favorite": line_item.product.favorite,
                    "image": line_item.product.images.first()
                },
            }
            line_items_dict.append(line_item_dict)
        return line_items_dict
