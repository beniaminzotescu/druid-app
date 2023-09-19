from django.db import models
from django.contrib.auth.models import User
import datetime


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    has_logged_in = models.BooleanField(default=False)
    timestamp = models.DateTimeField(default=datetime.datetime.now())
    last_login_datetime = models.DateTimeField(default=datetime.datetime.now())

    # Other fields specific to the user profile

    def __str__(self):
        return self.user.username
