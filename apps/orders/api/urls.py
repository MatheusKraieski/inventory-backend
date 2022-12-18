from django.urls import path
from apps.orders.api import viewsets


urlpatterns = [
    path('orders', viewsets.Orders.as_view()),
    path('orders/create_order', viewsets.Orders.as_view()),
]
