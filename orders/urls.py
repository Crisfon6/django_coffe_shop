from django.urls import path

from .views import MyOrderView, CreateOrderProductView, DeleteOrderProductView

urlpatterns = [
    path("my-order/", MyOrderView.as_view(), name="my_orders"),
    path("add-product/", CreateOrderProductView.as_view(), name="add_product"),
    path(
        "remove-order-product/<int:pk>",
        DeleteOrderProductView.as_view(),
        name="remove_order_product",
    ),
    path("", MyOrderView.as_view(), name="my_orders"),
]
