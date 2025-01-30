from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100,unique=True)
    discription = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
    
class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discount_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  
    product_image = models.ImageField(upload_to='product-image')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title