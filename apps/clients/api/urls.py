from django.urls import path
from apps.clients.api import viewsets


urlpatterns = [
    path('clients', viewsets.ClientList.as_view()),
    path('clients/<client_pk>', viewsets.ClientDetail.as_view()),
]
