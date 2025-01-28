from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView
from products.models import Product 
from .forms import ProductForm,ProductImage

class ProductFormView(generic.FormView):
    template_name = "products/add_product.html"
    form_class = ProductForm
    success_url = reverse_lazy('list_products')
    
    def form_valid(self, form):   
        
        form.save()
        return super().form_valid(form)

class ProductFormImageView(generic.FormView):
    template_name = "products/add_product.html"
    form_class = ProductImage    
    success_url = reverse_lazy('list_products')
    
    def form_valid(self, form) -> HttpResponse:
        print('Form: ')
        print(form.__dict__)
        form.save()
        return super().form_valid(form)

class ListProducts(generic.ListView):
    model = Product
    template_name= "products/list_products.html"
    context_object_name = "products"