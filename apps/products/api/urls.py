from django.urls import path
from apps.products.api import viewsets


urlpatterns = [
    path('products', viewsets.ProductList.as_view()),
    path('products/<product_pk>', viewsets.ProductDetail.as_view()),
]
