from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User
from tweets.models import Tweet

# Create your views here.
def users(request):
    myusers = User.objects.all().values()
    template = loader.get_template('all_users.html')

    context = {
        'myusers': myusers,
    }

    return HttpResponse(template.render(context, request))

def details(request, id):
    myuser = User.objects.get(id=id)
    tweets = Tweet.objects.all()

    user_tweets = []
    for tweet in tweets:
        if tweet.user_id == id:
            user_tweets.append(tweet)

    template = loader.get_template('details.html')

    context = {
        'myuser': myuser,
        'user_tweets': user_tweets
    }

    return HttpResponse(template.render(context, request))