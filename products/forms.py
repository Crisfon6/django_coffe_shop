from django import forms

from products.models import Product


class ProductForm(forms.Form):
    name = forms.CharField(label="Nombre", max_length=200)
    description = forms.CharField(label="Description", max_length=300)
    price = forms.DecimalField(label="Precio", max_digits=10, decimal_places=2)
    available = forms.BooleanField(label="Disponible", required=False,initial=True)
    photo = forms.ImageField(label="Foto", required=False)
    
    def save(self):
        Product.objects.create(
            name=self.cleaned_data['name'],
            description=self.cleaned_data['description'],
            price=self.cleaned_data['price'],
            available=self.cleaned_data['available'],
            photo=self.cleaned_data['photo']
        )
class ProductImage(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','description','price','available','photo']