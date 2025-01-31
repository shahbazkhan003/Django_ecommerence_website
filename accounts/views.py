from rest_framework import generics
from .models import Address
from .serializers import AddressSerializer
from rest_framework.permissions import IsAuthenticated

class AddressListCreate(generics.ListCreateAPIView):
    queryset = Address.objects.all()  
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  