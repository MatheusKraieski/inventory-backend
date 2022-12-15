from django.urls import include, path, re_path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    re_path(r'^admin/?', admin.site.urls),
    path('api/v1/', include('apps.cart.api.urls')),
    path('api/v1/', include('apps.orders.api.urls')),
    path('api/v1/', include('apps.products.api.urls')),
    path('api/v1/', include('apps.categories.api.urls')),
    path('api/v1/', include('apps.clients.api.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
