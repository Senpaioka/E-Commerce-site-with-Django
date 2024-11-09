from django.shortcuts import render

# Create your views here.

def cart_page_view(request):

    html_template_name = 'carts/cart.html'

    context = {}

    return render(request, html_template_name, context)