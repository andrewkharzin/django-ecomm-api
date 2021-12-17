from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("store.urls", namespace="store")),
    path('basket/', include('store.apps.basket.urls', namespace='basket')),
    path('account/', include('store.apps.account.urls', namespace='account')),
    path('payment/', include('store.apps.payment.urls', namespace='payment')),
    path('orders/', include('store.apps.orders.urls', namespace='orders')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
