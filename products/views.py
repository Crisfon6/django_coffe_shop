from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from rest_framework.views import APIView
from rest_framework.response import Response

from products.models import Product 
from .forms import ProductForm,ProductImage
from .serializers import ProductSerializer
class ProductFormView(generic.FormView):
    template_name = "products/add_product.html"
    form_class = ProductForm
    success_url = reverse_lazy('list_products')
    
    def form_valid(self, form):   
        print('Form: ')
        print(form.__dict__)
        form.save()
        return super().form_valid(form)

class ProductFormImageView(generic.FormView):
    template_name = 'products/add_product.html'
    form_class = ProductImage    
    success_url = reverse_lazy('list_products')
    
    def form_valid(self, form) -> HttpResponse:
        print('Form: ')
        print(form.__dict__)
        form.save()
        return super().form_valid(form)

class ListProducts(generic.ListView):
    model = Product
    template_name= 'products/list_products.html'
    context_object_name = 'products'

class ProductListAPI(APIView):
    authentication_classes = []
    parser_classes = []
    queryset = Product.objects.all()
    
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'