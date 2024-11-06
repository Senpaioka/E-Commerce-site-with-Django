from django.shortcuts import render, get_object_or_404
from store.models import Product
from category.models import Categories

# Create your views here.

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