from django.urls import path
from carts import views


app_name = 'carts'


urlpatterns = [
    path('cart_page/', views.cart_page_view, name='cart_page'),
]
