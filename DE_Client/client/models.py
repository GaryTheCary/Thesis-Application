from django.db import models
from django.db.models import IntegerField


class userName(models.Model):

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254, default='default@deuser.app')
    userID = models.CharField(max_length=20)
    user_age = IntegerField(default=0)
    create_time = models.DateTimeField('date created at')
    password = models.CharField(max_length=30, default='this is a default password')

    def __unicode__(self):
        # return the id of the current user when retrieving
        return self.userID

    def __str__(self):
        # get the actual readable string from the class
        return self.userID
