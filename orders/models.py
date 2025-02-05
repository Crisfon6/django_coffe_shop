from django.db import models
from django.contrib.auth.models import User

from products.models import Product

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    order_date = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'order: {self.id} by: {self.user}'

    def get_total(self):
        return sum(orderproduct.product.price * orderproduct.quantity for orderproduct in self.orderproduct_set.all())
    
class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    
    def __str__(self) -> str:
        return f'{self.product} x {self.quantity}'