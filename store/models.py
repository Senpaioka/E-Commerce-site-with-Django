from django.db import models
from category.models import Categories
from django.urls import reverse

# Create your models here.

class Product(models.Model):

    product_name = models.CharField(max_length=50)
    product_slug = models.SlugField(max_length=100)
    product_description = models.TextField(blank=True)
    product_price = models.IntegerField()
    product_img = models.ImageField(upload_to='photos/products')
    product_stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    
    category = models.ForeignKey(Categories, on_delete=models.PROTECT)
    
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)


    def get_urls(self):
        return reverse('store:product_details', args=[self.category.slug, self.product_slug])


    def __str__(self):
        return self.product_name
    

    
