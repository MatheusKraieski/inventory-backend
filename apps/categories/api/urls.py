from django.urls import path
from apps.categories.api import viewsets

urlpatterns = [
    path('categories', viewsets.CategoryView.as_view()),

]
