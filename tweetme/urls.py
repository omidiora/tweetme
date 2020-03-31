from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('tweet/<int:id>',views.tweet_detail_view),
    path('tweet',views.tweet_list_view),
]
