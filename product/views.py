from product.serializer import ProductSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from product.models import Product
from rest_framework import filters
import django_filters.rest_framework
from .models import Product
from .filters import ProductFilter  

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    filterset_class = ProductFilter  

class searchView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title' ]    
    