from django.urls import path
from product import views
urlpatterns = [
    path('product/',views.ProductListView.as_view(),name='products'),
    path('search/',views.searchView.as_view(),name="search"),
]
