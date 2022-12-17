from django.contrib import admin
from apps.line_items.models import LineItem
from apps.cart.models import Cart


class LineItemInline():
    model = LineItem

# Register your models here.
admin.site.register(Cart)