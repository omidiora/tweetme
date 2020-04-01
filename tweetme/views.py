from django import forms
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins  import LoginRequiredMixin

from django.views.generic import DetailView,ListView,CreateView,UpdateView
from .forms import TweetModelForm
from .mixins import  FormUserNeededMixin
from .models import Tweet


# Create your views here.

def home(request):
    return render(request,'home.html')



class TweetCreateView(LoginRequiredMixin, FormUserNeededMixin,CreateView):
    form_class=TweetModelForm
    template_name='tweetme/create_view.html'
    success_url="/tweet/create"
    login_url='/admin/'

class TweetUpdateView(UpdateView):
    queryset=Tweet.objects.all()
    form_class=TweetModelForm
    template_name='tweetme/update_view.html'
    success_url="/tweet"

   

class TweetDetailView(DetailView):
    
    queryset=Tweet.objects.all()



class TweetListView(ListView):
    
    queryset=Tweet.objects.all()

    def get_context_data(self,*args,**kwargs):
        context=super(TweetListView,self).get_context_data(*args,**kwargs)
        return context
    


def tweet_detail_view(request,id=1):
    obj=Tweet.objects.get(id=id)
    context={'object':obj}
    return render(request,'tweet/detail_view.html',context)


def tweet_list_view(request):
    queryset=Tweet.objects.all()
    context={'object_list':queryset}
    return render(request,'tweet/list_view.html',context)