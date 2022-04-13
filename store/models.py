from django.db import models
from django.urls import reverse

from category.models import Category    # importa la clase Category de la app category - category/models.py

# Create your models here.
class Product(models.Model):
    product_name    = models.CharField(max_length=200, unique=True)
    slug            = models.SlugField(max_length=200, unique=True)
    description     = models.TextField(max_length=200, unique=True)
    price           = models.IntegerField()
    images          = models.ImageField(upload_to='photo/products')
    stock           = models.IntegerField()
    is_available    = models.BooleanField(default=True)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)

    def get_url(self):
        # product_detail, ruta del detalle del producto en 'store/url.py'
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name

