from django.urls import path
from apps.cart.api import viewsets

urlpatterns = [
    path('cart/<cart_id>', viewsets.GetCurrentCart.as_view()),
    path('cart/line_items/add_to_cart', viewsets.AddLineItemToCart.as_view()),
]
