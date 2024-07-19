from django.db import models
from users.models import User
from tweets.models import Tweet
from comments.models import Comment

class Like(models.Model):
    TWEET = 'tweet'
    COMMENT = 'comment'
    CONTENT_TYPE_CHOICES = [
        (TWEET, 'Tweet'),
        (COMMENT, 'Comment'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, null=True, blank=True, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, null=True, blank=True, on_delete=models.CASCADE)
    date_liked = models.DateField(auto_now_add=True)
    type = models.CharField(max_length=10, choices=CONTENT_TYPE_CHOICES, default=TWEET)

    def save(self, *args, **kwargs):
        if self.tweet:
            self.type = self.TWEET
            self.comment = None
        elif self.comment:
            self.type = self.COMMENT
            self.tweet = None
        else:
            raise ValueError("A like must reference either a tweet or a comment.")
        super().save(*args, **kwargs)
