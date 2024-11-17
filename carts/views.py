from django.shortcuts import render, redirect, get_object_or_404
from utils.user_session import _user_session_id
from store.models import Product, ProductVariation
from carts.models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def cart_page_view(request, total=0, quantity=0, cart_items=None):

    html_template_name = 'carts/cart.html'

    try:
        get_user_session_id = Cart.objects.get(cart_id=_user_session_id(request))
        cart_items = CartItem.objects.filter(cart=get_user_session_id, is_active=True)

        for item in cart_items:
            total += (item.product.product_price * item.quantity)
            quantity += item.quantity

        # applying 2% of tax in total purchase
        tax_amount = (2 * total) / 100
        pay_amount = total + tax_amount


    except ObjectDoesNotExist:
        pass
    
    context = {
        'total_price': total,
        'quantity': quantity,
        'cart_product_info': cart_items,
        'tax' : tax_amount,
        'total_pay' : pay_amount,
    }

    return render(request, html_template_name, context)




def add_product_to_cart(request, product_id):


    product_variation_list = []
    product = Product.objects.get(pk=product_id)

    if request.method == 'POST':
        
        for data in request.POST:
            key = data
            value = request.POST[key]

            try:
                get_product_variation = ProductVariation.objects.get(product=product, product_variation__iexact=key, variation_value__iexact=value)
                product_variation_list.append(get_product_variation)
            except:
                pass



    try:
        user_session = Cart.objects.get(cart_id=_user_session_id(request))

    except Cart.DoesNotExist:
        user_session = Cart.objects.create(
            cart_id = _user_session_id(request)
        )
    user_session.save()


    try:
        cart_item = CartItem.objects.get(product=product, cart=user_session)
        cart_item.quantity += 1
        cart_item.save()

    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product = product,
            cart = user_session,
            quantity = 1
        ) 
        cart_item.save()

    return redirect('carts:cart_page')





def remove_product_from_cart(request, product_id):
    
    get_user_session_id = Cart.objects.get(cart_id=_user_session_id(request))
    get_product = get_object_or_404(Product, pk=product_id)

    cart_item = CartItem.objects.get(product=get_product, cart=get_user_session_id)

    if cart_item.quantity > 1 :
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('carts:cart_page')








def delete_product_from_cart(request, product_id):
    
    get_user_session_id = Cart.objects.get(cart_id=_user_session_id(request))
    get_product = get_object_or_404(Product, pk=product_id)
    cart_item = CartItem.objects.get(product=get_product, cart=get_user_session_id)
    cart_item.delete()

    return redirect('carts:cart_page')