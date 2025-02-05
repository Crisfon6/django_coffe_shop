from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import OrderProductForm
from .models import Order, OrderProduct

# Create your views here.
class MyOrderView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'orders/my_order.html'
    context_object_name = 'orders'
    
    def get_object(self, queryset=None):
        return Order.objects.filter(is_active=True,user=self.request.user)
    
class CreateOrderProductView(LoginRequiredMixin, CreateView):
    template_name = 'orders/add_product.html'
    form_class =  OrderProductForm
    success_url = reverse_lazy('my_orders')
    
    def form_valid(self, form):
        order, _ = Order.objects.get_or_create(
            is_active = True,
            user= self.request.user
        )
        form.instance.order = order
        form.quantity = 1
        form.save()
        return super().form_valid(form)

class DeleteOrderProductView(LoginRequiredMixin,DeleteView):
    model = OrderProduct
    success_url = reverse_lazy('my_orders')
    
    def get_queryset(self):
        return OrderProduct.objects.filter(order__user=self.request.user)