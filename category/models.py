from django.db import models
from django.urls import reverse

# Create your models here.

class Categories(models.Model):

    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    category_img = models.ImageField(upload_to='photos/categories')


    class Meta:

        verbose_name = 'category'
        verbose_name_plural = 'categories'

    # return urls of category list with category slug as args
    def get_urls(self):
        return reverse('store:product_by_category', args=[self.slug])


    def __str__(self):
        return self.category_name
    




