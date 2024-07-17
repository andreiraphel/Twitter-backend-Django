from django.db import models
from users.models import User
from tweets.models import Tweet

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    date_liked = models.DateField(auto_now_add=True)