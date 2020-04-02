from django.urls import path
from django.views.generic.base import RedirectView
from .views import TweetListAPIView
app_name="tweetme"
urlpatterns = [
   path('',TweetListAPIView.as_view(),name="list")
]
