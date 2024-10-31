from django.shortcuts import render

# Create your views here.

def home_view(request):

    html_template_name = 'home/index.html'
    context = {}
    return render(request, html_template_name, context)
