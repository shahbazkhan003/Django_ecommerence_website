from .models import *
from .serializers import *
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import generics


class AddToCart(generics.CreateAPIView):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemSerializer

    def perform_create(self, serializer):
        product_id = self.request.data.get('prod_id')
        product = get_object_or_404(Product, id=product_id)
        serializer.save(user=self.request.user, product=product)

class CartList(generics.ListAPIView):
    serializer_class = OrderItemSerializer
    def get_queryset(self):
        return OrderItems.objects.filter(user=self.request.user)

    def list(self, request, *args, **kwargs):
        cart = self.get_queryset()
        amount = sum(p.quantity * p.product.discount_price for p in cart)
        shipping_amount = 70.0
        total_amount = amount + shipping_amount if cart.exists() else 0
        serializer = self.get_serializer(cart, many=True)
        return Response({
            'cart': serializer.data,
            'amount': amount,
            'total_amount': total_amount
        })

class PlusCart(generics.UpdateAPIView):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemSerializer
    def update(self, request, *args, **kwargs):
        prod_id = request.GET.get('prod_id')
        cart_item = OrderItems.objects.filter(user=request.user, product=prod_id).first()
        if cart_item:
            cart_item.quantity += 1
            cart_item.save()
            amount = sum(p.quantity * p.product.discount_price for p in OrderItems.objects.filter(user=request.user))
            shipping_price = 70.0
            total_amount = amount + shipping_price
            data = {
                'quantity': cart_item.quantity,
                'amount': amount,
                'total_amount': total_amount,
            }
            return Response(data)

class MinusCart(generics.UpdateAPIView):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemSerializer

    def put(self, request, *args, **kwargs):
        prod_id = request.GET.get('prod_id')
        cart_item = OrderItems.objects.filter(user=request.user, product=prod_id).first()  
        if cart_item:
            cart_item.quantity = max(0, cart_item.quantity - 1)
            cart_item.save()
        shipping_price = 70.0
        amount = sum(p.quantity * p.product.discount_price for p in OrderItems.objects.filter(user=request.user))
        return Response({
            'quantity': cart_item.quantity if cart_item else 0,
            'amount': amount,
            'total_amount': amount + shipping_price,
        })

class RemoveCart(generics.DestroyAPIView):
    queryset = OrderItems.objects.all()

    def delete(self, request, *args, **kwargs):
        prod_id = request.GET.get('prod_id')
        cart_item = OrderItems.objects.filter(user=request.user, product=prod_id).first()
        if cart_item:
            cart_item.delete()

class OrdersList(generics.ListAPIView):
    serializer_class = OrderPlacedSerializer
    def get_queryset(self):
        return OrderPlaced.objects.filter(user=self.request.user)

class Checkout(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        user = request.user
        address = Address.objects.filter(user=user)
        cart_products = OrderItems.objects.filter(user=user).select_related('product')
        sniping_price = 70.0
        total_amount = sum([item.quantity * item.product.discount_price for item in cart_products]) + sniping_price
        response_data = {
            'total_amount': total_amount,
            'address': list(address.values()), 
            'cart_items': list(cart_products.values(
                'id',
                'product__title',
                'quantity',
                'product__discount_price'
            )) 
        }
        return Response(response_data)

class PaymentDone(generics.CreateAPIView):
    serializer_class = OrderPlacedSerializer

    def post(self, request, *args, **kwargs):
        customer = get_object_or_404(Address, id=request.data.get('custid'))
        cart_items = OrderItems.objects.filter(user=request.user)
        
        for cart_item in cart_items:
            serializer = self.get_serializer(data={
                "user": request.user.id,
                "customer": customer.id,
                "address": customer.id,
                "product": cart_item.product.id,
                "quantity": cart_item.quantity
            })
            if serializer.is_valid():
                serializer.save()
                cart_item.delete()
        
  


