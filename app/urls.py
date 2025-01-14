from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('s',views.simple_view,name="s")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)