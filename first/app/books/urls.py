from django.urls import path
from .views import BookList, BookInfo

urlpatterns = [
    path('', BookList.as_view()),
    path('<int:pk>', BookInfo.as_view()),
]