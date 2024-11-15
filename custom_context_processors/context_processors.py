from category.models import Categories


# getting all category by name
# calling 'menu_links' in a for loop in the 'navbar.html' will avail all the category model data 
def category_list_for_menubar(request):

    category_queryset = Categories.objects.all()
    return dict(menu_links=category_queryset)








# get total number of cart item for menu bar cart icon
from carts.models import Cart, CartItem
from utils.user_session import _user_session_id


def cart_product_counter(request):

    cart_product_count = 0

    if 'admin' in request.path:
        return {}
    
    else:
        try:
            cart = Cart.objects.filter(cart_id=_user_session_id(request))
            cart_item = CartItem.objects.all().filter(cart=cart[:1])

            for item in cart_item:
                cart_product_count += item.quantity

        except Cart.DoesNotExist:
            cart_product_count = 0

    return dict(cart_product_count=cart_product_count)





