from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name= 'home'),
    path('category/<slug:category_slug>', views.home, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>', views.product, name="product_detail"),
    path('cart', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>', views.add_cart, name='add_cart'),
    path('cart/remove/<int:product_id>', views.cart_remove, name='cart_remove'),
    path('cart/remove_product/<int:product_id>', views.cart_remove_product, name='cart_remove_product'),
    path('account/create/', views.signUpView, name='signup'),
    path('account/login/', views.loginView, name='login'),
    path('account/signout/', views.signoutView, name='signout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
	urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
