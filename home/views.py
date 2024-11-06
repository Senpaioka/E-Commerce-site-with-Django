from django.shortcuts import render
from store.models import Product

# Create your views here.

def home_view(request):

    html_template_name = 'home/index.html'

    available_products = Product.objects.all().filter(is_available = True)

    context = {
        'products': available_products,
    }
    
    return render(request, html_template_name, context)
