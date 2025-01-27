from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    locality = models.CharField(max_length=200)  
    city = models.CharField(max_length=200)
    zip_code = models.IntegerField()
    state = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id)
