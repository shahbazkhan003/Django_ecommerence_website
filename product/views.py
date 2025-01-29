from product.serializer import ProductSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from product.models import Product
    
class Listapi(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

class Mobileapi(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]         
    def get_queryset(self):
        return Product.objects.filter(category='M')
    
class Laptopapi(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    def get_queryset(self):
        return Product.objects.filter(category='L')
    
class Topwearapi(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    def get_queryset(self):
        return Product.objects.filter(category='TW')
    
class Buttomwearapi(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    def get_queryset(self):
        return Product.objects.filter(category='BW')        
    
    
class SearchProductAPI(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        keyword = self.request.GET.get('keyword', '')
        return Product.objects.filter(title__icontains=keyword).order_by("-created_date") if keyword else Product.objects.none()
    