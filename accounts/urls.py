from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_registration.api.urls import register
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import AddressViewSet
router = DefaultRouter()
router.register(r'addresses', AddressViewSet, basename='address')

urlpatterns = [    
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', register, name='register'),
    path('', include(router.urls)),
]

