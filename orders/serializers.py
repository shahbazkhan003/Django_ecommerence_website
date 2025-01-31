from rest_framework import serializers
from .models import  OrderPlaced, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"
        extra_kwargs = {
            'user': {'required': False},
            'product': {'required': False}  
        }

    def validate_quantity(self, value):
        if value < 1:
            raise serializers.ValidationError("Quantity must be at least 1.")
        return value

class OrderPlacedSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)  

    class Meta:
        model = OrderPlaced
        fields = "__all__"

            