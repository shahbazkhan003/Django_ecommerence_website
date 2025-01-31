from django.urls import path
from orders import views
urlpatterns = [
    path('addtocart/',views.AddToCart.as_view(),name='addtocart'),
    path('cartlist/', views.CartList.as_view(), name='cartlist'),
    path('remove/', views.RemoveCart.as_view(), name='remove'),
    path('order/', views.OrdersList.as_view(),name="order" ),
    path('plus/', views.PlusCart.as_view(),name="pluscart"),
    path('minus/', views.MinusCart.as_view(),name="minuscart"),
    path('checkout/', views.Checkout.as_view(),name="checkout"),
    path('payment/', views.PaymentDone.as_view(), name='payment-done-api'),
]
