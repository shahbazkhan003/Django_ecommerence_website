from django.db import models

CATAGERY_CHOICE = (
    ('M', 'Mobile'),
    ('L', 'Laptop'),
    ('TW', 'Top Wear'),
    ('BW', 'Bottom Wear')
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discount_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(max_length=2, choices=CATAGERY_CHOICE)  
    product_image = models.ImageField(upload_to='productimg')
    created_date = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return str(self.id)