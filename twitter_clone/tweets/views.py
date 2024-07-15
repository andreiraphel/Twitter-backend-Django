from django.shortcuts import render
from tweets.models import Tweet

def tweets(request):
    mytweets = Tweet.objects.all()
    return render(request, 'all_tweets.html', {'mytweets': mytweets})
