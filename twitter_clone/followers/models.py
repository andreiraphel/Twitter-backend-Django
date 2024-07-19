from django.db import models
from users.models import User

class Follow(models.Model):
    user = models.ForeignKey(User, related_name='following' ,on_delete=models.CASCADE)
    followed_user = models.ForeignKey(User, related_name='followers' ,on_delete=models.CASCADE)
    date_followed = models.DateField(auto_now_add=True, null=True)

    class Meta:
        unique_together = ('user', 'followed_user')