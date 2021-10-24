from django.contrib import admin

# Register your models here.
from .models import ProductCategory, Product

# Register your models here.
admin.site.register(ProductCategory)
admin.site.register(Product)
