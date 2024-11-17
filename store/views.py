from django.shortcuts import render, get_object_or_404
from store.models import Product
from category.models import Categories
from carts.models import CartItem
from utils.user_session import _user_session_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q

# Create your views here.

# store page
def store_page_view(request, category_slug=None):

    html_template_name = 'store/store.html'    

    selected_category = None
    all_product = None

    if category_slug != None:
        selected_category = get_object_or_404(Categories, slug=category_slug)
        all_product = Product.objects.filter(category=selected_category, is_available=True).order_by('id')
        
        # paginator functionality
        paginator = Paginator(all_product, 6)
        page = request.GET.get('page')
        set_page = paginator.get_page(page)

        product_count = all_product.count()

    else:
        all_product = Product.objects.all().filter(is_available = True).order_by('id')
        
        # paginator functionality
        paginator = Paginator(all_product, 6)
        page = request.GET.get('page')
        set_page = paginator.get_page(page)

        product_count = all_product.count()

    context = {
        'products': set_page,
        'count': product_count,
    }

    return render(request, html_template_name, context)









# product details
def product_details_page(request, category_slug, selected_product_slug):
    
    html_template_name = 'store/product_details.html'

    try:
        single_product = Product.objects.get(category__slug=category_slug, product_slug=selected_product_slug)
        cart_empty_or_not = CartItem.objects.filter(cart__cart_id=_user_session_id(request), product=single_product).exists()
    except Exception as err:
        raise err

    context = {
        'product_info' : single_product,
        'is_cart_available': cart_empty_or_not,
    }

    return render(request, html_template_name, context)








def search_functionality_view(request):

    html_template_name = 'store/store.html'

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']

        if keyword is not " ":
            searched_product = Product.objects.order_by('-created_date').filter(Q(product_description__icontains=keyword) | Q(product_name__icontains=keyword))
            found_product = searched_product.count()
    context = {
        'products' : searched_product,
        'count': found_product,
    }

    return render(request, html_template_name, context)