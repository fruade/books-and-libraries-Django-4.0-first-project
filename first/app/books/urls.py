from django.urls import path
from .views import BookList, BookInfo, BookFormView
from django_filters.views import FilterView


urlpatterns = [
    path('', BookList.as_view(), name='books'),
    path('add_book', BookFormView.as_view(), name='add_book'),
    path('<int:pk>', BookInfo.as_view(), name='detail_book'),
]