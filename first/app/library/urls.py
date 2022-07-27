from django.urls import path
from .views import LibraryList, LibraryInfo, LibraryFormView

urlpatterns = [
    path('', LibraryList.as_view(), name='libraries'),
    path('add_library', LibraryFormView.as_view(), name='add_library'),
    path('<int:pk>', LibraryInfo.as_view(), name='detail_library'),
]