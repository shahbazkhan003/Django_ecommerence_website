from rest_framework import serializers
from .models import Order, OrderItems

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = ['id', 'product', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'address', 'order_date', 'status', 'items']