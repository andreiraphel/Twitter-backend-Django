from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import User
from tweets.models import Tweet
from likes.models import Like
from comments.models import Comment
from followers.models import Follow
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    template = loader.get_template('register.html')
    context = {
        'registerform': form,
    }

    return HttpResponse(template.render(context, request))

def login_view(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect("main")
                
    template = loader.get_template('login.html')
    context = {
        'loginform': form,
    }

    return HttpResponse(template.render(context, request))

def user_logout(request):
    auth.logout(request)
    return redirect("login")

@login_required(login_url="login")
def users(request):
    myusers = User.objects.all().values()
    template = loader.get_template('all_users.html')

    context = {
        'myusers': myusers,
    }

    return HttpResponse(template.render(context, request))

@login_required(login_url="login")
def details(request, user_id):
    myuser = User.objects.get(id=user_id)
    tweets = Tweet.objects.filter(user_id=myuser.id)
    following = Follow.objects.filter(user_id=myuser.id)
    followers = Follow.objects.filter(followed_user=myuser.id)

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'delete_tweet':
            tweet_id = request.POST.get('tweet_id')
            Tweet.objects.filter(id=tweet_id).delete()
            next_url = request.POST.get('next', '/')
            return redirect(next_url)

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

@login_required(login_url="login")
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

@login_required(login_url="login")
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

@login_required(login_url="login")
def main(request):
    following = Follow.objects.filter(user_id=request.user.id)

    following_ids = [follow.followed_user_id for follow in following]

    following_tweets = Tweet.objects.filter(user_id__in=following_ids)
    my_tweets = Tweet.objects.filter(user_id=request.user.id)

    all_tweets = (following_tweets | my_tweets).order_by('tweet_created')

    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'create_tweet':
            tweet = request.POST.get('tweet')
            new_tweet = Tweet(user_id=request.user.id, tweet=tweet)
            new_tweet.save()
            return redirect("main")

        elif action == 'delete_tweet':
            tweet_id = request.POST.get('tweet_id')
            Tweet.objects.filter(id=tweet_id).delete()
            next_url = request.POST.get('next', '/')
            return redirect(next_url)


    comment_counter = {}
    tweet_likes = {}

    for tweet in all_tweets:
        tweet_likes[tweet.id] = Like.objects.filter(tweet_id=tweet.id).count()
        comment_counter[tweet.id] = Comment.objects.filter(tweet_id=tweet.id).count()

    context = {
        'tweets': all_tweets,
        'tweet_likes': tweet_likes,
        'comment_counter': comment_counter,
    }

    return render(request, 'main.html', context=context)
