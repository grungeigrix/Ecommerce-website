from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name= 'home'),
    path('<slug:category_slug>', views.home, name='products_by_category'),
    path('product/', views.product, name="product"),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
	urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)