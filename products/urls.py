from django.urls import path

from products.views import products

app_name = 'products'

urlpatterns = [
    path('', products, name='product'),
    path('category/<int:pk>/', products, name='category'),
    path('product/<int:pk>/', products, name='detail'),
    path('category/<int:pk>/page/<int:page>/', products, name='page'),
]
