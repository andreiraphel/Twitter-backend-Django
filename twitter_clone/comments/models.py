from django.db import models
from users.models import User
from tweets.models import Tweet

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    comment_created = models.DateField(auto_now_add=True, null=True)
    type = models.CharField(max_length=10, default='comment')