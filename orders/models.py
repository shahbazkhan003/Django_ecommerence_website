from django.db import models
from product.models import Product
from accounts.models import CustomUser, Address


class StateChoices(models.TextChoices):
    PENDING = 'Pending', 'Pending'
    ACCEPTED = 'Accepted', 'Accepted'
    PACKED = 'Packed', 'Packed'
    ON_THE_WAY = 'On The Way', 'On The Way'
    DELIVERED = 'Delivered', 'Delivered'
    CANCELLED = 'Cancel', 'Cancel'

class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=StateChoices.choices, default=StateChoices.PENDING)

    def __str__(self):
        return str(self.id)
    
class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    