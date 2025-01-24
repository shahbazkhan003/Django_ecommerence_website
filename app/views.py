from .models import *
from .serializers import *
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework import generics

class product_view(generics.ListAPIView):
    @permission_classes([AllowAny])  
    def list(self, request, *args, **kwargs):
        topwears = Product.objects.filter(category='TW')
        jeans = Product.objects.filter(category='BW')
        mobiles = Product.objects.filter(category='M')
        laptops = Product.objects.filter(category='L')

        data = {
            'topwears': ProductSerializer(topwears, many=True).data,
            'jeans': ProductSerializer(jeans, many=True).data,
            'mobiles': ProductSerializer(mobiles, many=True).data,
            'laptops': ProductSerializer(laptops, many=True).data,
        }
        return Response(data)

class product_detail_api(generics.RetrieveAPIView):
    @permission_classes([AllowAny])  
    def retrieve(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        product = get_object_or_404(Product, pk=pk)
        item_already_in_cart = False
        if request.user.is_authenticated:
            item_already_in_cart = Cart.objects.filter(product=product.id, user=request.user).exists()
        data = {
            'product': ProductSerializer(product).data,
            'item_already_in_cart': item_already_in_cart,
        }
        return Response(data)  
    
class mobile_api(generics.ListAPIView):
    @permission_classes([AllowAny])  
    def list(self, request,data=None):
        mobiles = Product.objects.filter(category='M') 
        mobile_data = list(mobiles.values('id', 'title', 'brand','description' ,'selling_price','discount_price', 'category','created_date','product_image'))
        return Response({"mobiles": mobile_data}, status=200)


class laptop_api(generics.ListAPIView):
    @permission_classes([AllowAny])  
    def list(self, request,data=None):
        laptops = Product.objects.filter(category='L')
        laptop_data =list(laptops.values('id', 'title', 'brand','description' ,'selling_price','discount_price', 'category','created_date','product_image'))  
        return Response({'laptop_data' : laptop_data},status=200)

class topwear_api(generics.ListAPIView):
    @permission_classes([AllowAny])
    def list(self, request):
        topwears = Product.objects.filter(category='TW')
        topwear_data =list(topwears.values('id', 'title', 'brand','description' ,'selling_price','discount_price', 'category','created_date','product_image')) 
        return Response({'topwear_data' : topwear_data},status=200)

class buttomwear_api(generics.ListAPIView):
    @permission_classes([AllowAny])
    def list(self, request):
        buttomwear = Product.objects.filter(category='BW')
        buttomwear_data =list(buttomwear.values('id', 'title', 'brand','description' ,'selling_price','discount_price', 'category','created_date','product_image')) 
        return Response({'buttomwear_data' : buttomwear_data},status=200)    