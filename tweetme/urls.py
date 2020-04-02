from django.urls import path
from . import views
app_name="tweetme"
urlpatterns = [
    path('',views.home),
    path('tweet/<int:pk>',views.TweetDetailView.as_view(),name='detail'),
    path('tweet/create/',views.TweetCreateView.as_view(),name='create'),
    path('tweet',views.TweetListView.as_view(),name='list'),
    path('tweet/update/<int:pk>/',views.TweetUpdateView.as_view(),name="update"),
    path('tweet/delete/<int:pk>/',views.TweetDeleteView.as_view(),name="delete"),
]
