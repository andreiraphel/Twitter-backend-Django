from django.shortcuts import render
from tweets.models import Tweet
from users.models import User

def tweets(request):
    mytweets = Tweet.objects.all()
    myusers = User.object.all().values('id', 'username')
    return render(request, 'all_tweets.html', {'mytweets': mytweets, 'myusers': myusers})


