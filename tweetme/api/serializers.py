from rest_framework import serializers
from tweetme.models import Tweet
from accounts.api.serializers import UserDisplaySerializer


class TweetModelSerializer(serializers.ModelSerializer):
    user=UserDisplaySerializer()  
    class Meta:
        model=Tweet
        fields=[
            'user',
            'content',
        ]