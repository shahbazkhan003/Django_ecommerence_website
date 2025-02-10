from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Order, OrderItems
from .serializers import OrderSerializer, OrderItemSerializer
from product.models import Product
from accounts.models import Address

class CreateOrder(generics.CreateAPIView):
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        user = request.user
        address = get_object_or_404(Address, id=request.data.get('address_id'), user=user)
        items_data = request.data.get('items', [])
        if not items_data:
            return Response({'error': 'No items provided'}, status=400)
        order = Order.objects.create(user=user, address=address)
        for item_data in items_data:
            product = get_object_or_404(Product, id=item_data.get('product_id'))
            OrderItems.objects.create(order=order, product=product, quantity=item_data.get('quantity', 1))

        serializer = self.get_serializer(order)
        return Response(serializer.data)

class OrdersList(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)