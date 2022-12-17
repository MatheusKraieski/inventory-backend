from django.urls import path
from apps.clients.api import viewsets


urlpatterns = [
    path('line_items', viewsets.ClientList.as_view()),
    
]
