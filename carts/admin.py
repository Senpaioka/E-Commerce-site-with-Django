from django.contrib import admin
from carts.models import Cart, CartItem
# Register your models here.


admin.site.register(Cart)


class CartItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'cart' ,'quantity']


admin.site.register(CartItem, CartItemAdmin)
