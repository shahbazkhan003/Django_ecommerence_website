from django.urls import path,include
from . import views

api_urlpatterns = [
    path('accounts/', include('rest_registration.api.urls')),
]

urlpatterns = [    
]

