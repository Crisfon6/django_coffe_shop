from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.TextField(max_length=200, verbose_name="nombre")
    description = models.TextField(max_length=300, verbose_name="descripcion")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="precio")
    available = models.BooleanField(default=True, verbose_name="disponible")
    photo = models.ImageField(upload_to='products/photos/', verbose_name="foto",null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="creado")
    
    def __str__(self) -> str:
        return self.name