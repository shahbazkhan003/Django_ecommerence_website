from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer


class CreateOrder(generics.CreateAPIView):
    serializer_class = OrderSerializer


class OrdersList(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)