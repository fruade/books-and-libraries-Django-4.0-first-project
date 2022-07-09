from django.urls import path
from .views import LibraryList, LibraryInfo

urlpatterns = [
    path('', LibraryList.as_view()),
    path('<int:pk>', LibraryInfo.as_view()),
]