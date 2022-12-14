from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('api/v1/', include('apps.cart.api.urls')),
    path('api/v1/', include('apps.orders.api.urls')),
    path('api/v1/', include('apps.products.api.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
