from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('api/products/', views.product_view.as_view(), name='product_api'),
    path('api/product-detail/<int:pk>', views.product_detail_api.as_view(), name='product-detail-api'),
    path('api/add-to-cart/', views.add_to_cart_api.as_view(), name='add-to-cart'),
    path('api/cart/',views.show_cart.as_view(),name='showcart'),
    path('api/pluscart/<int:pk>',views.plus_cart_api.as_view()),
    path('api/minuscart/<int:pk>',views.minus_cart_api.as_view()),
    path('api/removecart/<int:pk>',views.remove_cart_api.as_view()),
    path('api/profile/', views.profile_api.as_view(), name='profile'),
    path('api/address/', views.address_api.as_view(), name='address'),
    path('api/orders/', views.orders_api.as_view(), name='orders'),
    path('api/mobile/', views.mobile_api.as_view(), name='mobile'),
    path('api/mobile/<slug:data>', views.mobile_api.as_view(), name='mobiledata'),
    path('api/laptop/', views.laptop_api.as_view(), name='laptop'),
    path('api/laptopdata/<slug:data>', views.laptop_api.as_view(), name='laptopdata'),
    path('api/topwear/', views.topwear_api.as_view(), name='topwear'),
    path('api/buttomwear/', views.buttomwear_api.as_view(), name='buttomwear'),
    path('api/checkout/', views.checkout_api.as_view(), name='checkout'),
    path('api/paymentdone/', views.payment_done_api.as_view(), name='paymentdone'),
    path('api/search/<int:pk>',views.search_api.as_view(),name='search')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)