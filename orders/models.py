from django.db import models
from product.models import Product
from accounts.models import CustomUser,Address

class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

def __str__(self):
    return str(self.id)

STATE_CHOICE = (
    ('Accepted', 'Accepted'),
    ('Paked' , 'Packed'),
    ('On The Way' , 'On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel')
)    

class OrderPlaced(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATE_CHOICE, default='Pending')
    
    def __str__(self):
        return str(self.id)
