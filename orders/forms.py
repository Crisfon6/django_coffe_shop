from django.forms import Form, ModelForm
from django import forms

from products.models import Product
from .models import OrderProduct

class OrderProductForm(ModelForm):
    class Meta:
        model = OrderProduct
        fields = ['product','quantity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-input'})
    