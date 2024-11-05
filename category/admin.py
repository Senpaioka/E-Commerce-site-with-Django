from django.contrib import admin
from category.models import Categories

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ['category_name']}
    # list_display = []


admin.site.register(Categories, CategoryAdmin)