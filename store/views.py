from django.shortcuts import render, get_object_or_404
from store.models import Product
from category.models import Categories

# Create your views here.

# store page
def store_page_view(request, category_slug=None):

    html_template_name = 'store/store.html'    

    selected_category = None
    all_product = None

    if category_slug != None:
        selected_category = get_object_or_404(Categories, slug=category_slug)
        all_product = Product.objects.filter(category=selected_category, is_available=True)
        product_count = all_product.count()

    else:
        all_product = Product.objects.all().filter(is_available = True)
        product_count = all_product.count()

    context = {
        'products': all_product,
        'count': product_count,
    }

    return render(request, html_template_name, context)









# product details
def product_details_page(request, category_slug, selected_product_slug):
    
    html_template_name = 'store/product_details.html'

    try:
        single_product = Product.objects.get(category__slug=category_slug, product_slug=selected_product_slug)
    except Exception as err:
        raise err

    context = {
        'product_info' : single_product,
    }

    return render(request, html_template_name, context)