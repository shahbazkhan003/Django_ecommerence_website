from rest_framework import serializers
from orders.models import *
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__" 
        extra_kwargs = {
            'user': {'required': False},
            'product': {'required': False}  
        }
        
class OrderPlacedSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderPlaced
        fields = "__all__"                        
        