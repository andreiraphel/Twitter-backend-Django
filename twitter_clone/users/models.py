from django.db import models

class User(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, null=True)
    username = models.CharField(null=True, max_length=254)
    joined_date = models.DateField(auto_now_add=True, null=True)