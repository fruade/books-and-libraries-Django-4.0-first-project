from django.urls import path
from .views import library_start

urlpatterns = [
    path('', library_start),
]