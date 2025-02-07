from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from products.views import (
    ProductFormImageView,
    ProductFormView,
    ListProducts,
    ProductListAPI,
    ProductDetailView,
    ProductViewSet,
)

router = routers.DefaultRouter()
router.register(r"api", ProductViewSet)

urlpatterns = [
    path("add/", ProductFormView.as_view(), name="create_product"),
    # path('add2/', ProductFormImageView.as_view(), name="add_product2"),
    # path('api/', ProductViewSet, name="list_product_api"),
    path("", ListProducts.as_view(), name="list_products"),
    path("<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("", include(router.urls)),
]
