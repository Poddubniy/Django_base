from django.contrib import admin

# Register your models here.
from .models import ProductCategory, Product

# Register your models here.
admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'category', 'image', 'description', ('price', 'quantity'))
    readonly_fields = ('description',)
    # ordering = ('name',)   # -name
    search_fields = ('name',)
