from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .managers import CustomUserManager

class CustomUser(AbstractBaseUser,PermissionsMixin):

    class Roles(models.TextChoices):
        SELLER = "Seller", "Seller"
        MANAGER = "Manager", "Manager"
        BUYER = "Buyer", "Buyer"

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    role = models.CharField(max_length=50,choices=Roles.choices,default=Roles.BUYER)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name","role"]

class Address(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)  
    postal_code = models.IntegerField()
    

    def __str__(self):
        return self.name