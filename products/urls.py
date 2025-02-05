from django.contrib import admin
from django.urls import path

from products.views import ProductFormImageView, ProductFormView,ListProducts


urlpatterns = [
    path('agregar/', ProductFormView.as_view(), name="add_product"),
     path('agregar2/', ProductFormImageView.as_view(), name="add_product2"),
    path('', ListProducts.as_view(), name='list_products'),
]
