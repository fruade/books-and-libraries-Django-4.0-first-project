from django.urls import path
from .views import get_books_list, get_books_id

urlpatterns = [
    path('', get_books_list),
    path('<int:id_book>', get_books_id),
]