from django.urls import path
from carts import views


app_name = 'carts'


urlpatterns = [
    path('cart_page/', views.cart_page_view, name='cart_page'),
    path('add_to_cart/<int:product_id>/', views.add_product_to_cart, name='add_cart'),
    path('remove_from_cart/<int:product_id>/', views.remove_product_from_cart, name='remove_cart'),
    path('delete_from_cart/<int:product_id>/', views.delete_product_from_cart, name='delete_cart'),
]
