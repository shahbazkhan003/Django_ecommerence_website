from rest_framework import serializers
from .models import  OrderPlaced, OrderItems

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
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

            