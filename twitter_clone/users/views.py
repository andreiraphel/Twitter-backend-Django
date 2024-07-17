from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User
from tweets.models import Tweet
from likes.models import Like

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
    likes = Like.objects.all()

    user_tweets = []
    tweet_likes = {}

    for tweet in tweets:
        if tweet.user_id == id:
            user_tweets.append(tweet)
            tweet_likes[tweet.id] = 0
            for like in likes:
                if like.tweet_id == tweet.id:
                    tweet_likes[tweet.id] += 1
                    tweet_id = tweet.id

    template = loader.get_template('details.html')
    print(tweet_likes)
    context = {
        'myuser': myuser,
        'user_tweets': user_tweets,
        'tweet_likes': tweet_likes,
        'tweet_id': tweet_id,
    }

    return HttpResponse(template.render(context, request))