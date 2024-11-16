from django.urls import path
from store import views


app_name = 'store'


urlpatterns = [
    path('store_page/', views.store_page_view, name='store_page'),
    path('store_page/<slug:category_slug>/', views.store_page_view, name='product_by_category'),
    path('store_page/<slug:category_slug>/<slug:selected_product_slug>/', views.product_details_page, name='product_details'),
    path('search/', views.search_functionality_view, name='search'),
]
