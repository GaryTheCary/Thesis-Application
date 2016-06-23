from django.db import models
from django.db.models import IntegerField

# this is the model that handle un-migratable models

class userLogin(models.Model):
    userID_email = models.CharField(max_length=200)
    password = models.CharField(max_length=8)