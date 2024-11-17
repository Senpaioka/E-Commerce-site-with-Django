from django.contrib import admin
from store.models import Product, ProductVariation
 

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'product_price', 'category', 'product_stock', 'is_available', 'modified_date']
    prepopulated_fields = {'product_slug': ['product_name']}

admin.site.register(Product, ProductAdmin)




class ProductVariationAdmin(admin.ModelAdmin):
    list_display = ['product', 'product_variation', 'variation_value', 'is_available']
    list_editable = ['is_available']
    list_filter = ['product', 'product_variation', 'variation_value']

admin.site.register(ProductVariation, ProductVariationAdmin)