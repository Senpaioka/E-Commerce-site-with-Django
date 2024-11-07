from category.models import Categories


# getting all category by name
# calling 'menu_links' in a for loop in the 'navbar.html' will avail all the category model data 
def category_list_for_menubar(request):

    category_queryset = Categories.objects.all()
    return dict(menu_links=category_queryset)