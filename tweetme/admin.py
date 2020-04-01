from django.contrib import admin
from .models import *
from .forms import TweetModelForm
# Register your models here.
#admin.site.register(Tweet)

class TweetModelAdmin(admin.ModelAdmin):
    # class Meta:
    #     model=Tweet
        form=TweetModelForm

admin.site.register(Tweet,TweetModelAdmin)