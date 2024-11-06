from django.contrib import admin
from store.models import Product
 

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'product_price', 'category', 'product_stock', 'is_available', 'modified_date']
    prepopulated_fields = {'product_slug': ['product_name']}


admin.site.register(Product, ProductAdmin)