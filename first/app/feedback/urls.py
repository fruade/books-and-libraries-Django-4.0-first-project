from django.urls import path
from .views import get_feedback, done, FeedBackView

urlpatterns = [
    path('done', done, name='done'),
    path('', FeedBackView.as_view()),
    # path('', get_feedback),
]