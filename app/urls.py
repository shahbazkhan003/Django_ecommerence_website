from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('products/', views.product_view.as_view(), name='product'),
    path('product-detail/<int:pk>', views.product_detail_api.as_view(), name='product-detail'),
    path('mobile/', views.mobile_api.as_view(), name='mobile'),
    path('laptop/', views.laptop_api.as_view(), name='laptop'),
    path('topwear/', views.topwear_api.as_view(), name='topwear'),
    path('buttomwear/', views.buttomwear_api.as_view(), name='buttomwear'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)