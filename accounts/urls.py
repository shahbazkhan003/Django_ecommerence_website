from django.urls import path,include
from . import views

api_urlpatterns = [
    path('accounts/', include('rest_registration.api.urls')),
]
urlpatterns = [
    path('api/v1/', include(api_urlpatterns)),
    path('api/profile/', views.profile_api.as_view(), name='profile'),
    path('api/address/', views.address_api.as_view(), name='address'),
]


