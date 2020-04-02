from django.db import models
from django.conf import settings
from .validators import validate_content
from django.urls import reverse



class Tweet(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    content=models.CharField(max_length=140,validators=[validate_content])
    update=models.DateTimeField(auto_now_add=True)
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
        
    def get_absolute_url(self):
   
        return reverse('tweets:detail', kwargs={'pk': self.pk})