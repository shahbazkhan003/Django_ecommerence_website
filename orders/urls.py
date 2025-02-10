from django.urls import path
from .views import CreateOrder, OrdersList

urlpatterns = [
    path('create-order/', CreateOrder.as_view(), name='create-order'),
    path('orders/', OrdersList.as_view(), name='orders-list'),   
]  