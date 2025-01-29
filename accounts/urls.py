from django.urls import path,include
from . import views


urlpatterns = [    
    path('', include('rest_registration.api.urls')),
]

