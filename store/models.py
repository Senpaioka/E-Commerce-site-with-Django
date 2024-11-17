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
    












class VariationManager(models.Manager):

    def color_selected(self):
        return super(VariationManager, self).filter(product_variation='color', is_available=True)
    

    def size_selected(self):
        return super(VariationManager, self).filter(product_variation='size', is_available=True)




PRODUCT_VARIATIONS = [
    ('color', 'color'),
    ('size', 'size'),
]

class ProductVariation(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_variation = models.CharField(max_length=10, choices=PRODUCT_VARIATIONS)
    variation_value = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


    # set custom manager
    objects = VariationManager()


    def __str__(self):
        return self.product.product_name

    




    


    
