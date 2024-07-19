from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User
from tweets.models import Tweet
from likes.models import Like
from comments.models import Comment
from followers.models import Follow

# Create your views here.
def users(request):
    myusers = User.objects.all().values()
    template = loader.get_template('all_users.html')

    context = {
        'myusers': myusers,
    }

    return HttpResponse(template.render(context, request))

def details(request, user_id):
    myuser = User.objects.get(id=user_id)
    tweets = Tweet.objects.filter(user_id=myuser.id)
    following = Follow.objects.filter(user_id=myuser.id)
    followers = Follow.objects.filter(followed_user=myuser.id)

    following_count = following.count()
    followers_count = followers.count()

    comment_counter = {}
    tweet_likes = {}

    for tweet in tweets:
        tweet_likes[tweet.id] = Like.objects.filter(tweet_id=tweet.id).count()
        comment_counter[tweet.id] = Comment.objects.filter(tweet_id=tweet.id).count()

    print(followers_count)
    template = loader.get_template('details.html')
    
    context = {
        'myuser': myuser,
        'tweets': tweets,
        'tweet_likes': tweet_likes,
        'comment_counter': comment_counter,
        'followers_count': followers_count,
        'following_count': following_count,
    }

    return HttpResponse(template.render(context, request))

def liked(request, user_id, object_id):
    myusers = User.objects.all().values()
    likes = Like.objects.filter(tweet_id=object_id).values()

    template = loader.get_template('liked.html')
    users_liked_id = [x['user_id'] for x in likes]

    users_liked_list = [user for user in myusers if user['id'] in users_liked_id]

    print(users_liked_list)
    
    context = {
        'users_liked_list': users_liked_list,
        'user_id': user_id,
    }

    return HttpResponse(template.render(context, request))

def comments(request, user_id, object_id):
    myusers = User.objects.all().values()
    comment_dict = Comment.objects.filter(tweet_id=object_id).values()


    print(comment_dict)
    template = loader.get_template('comments.html')

    context = {
        'comment_dict': comment_dict,
        'user_id': user_id,
    }

    return HttpResponse(template.render(context, request))
