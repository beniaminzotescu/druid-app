from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    has_logged_in = models.BooleanField(default=False)

    # Other fields specific to the user profile

    def __str__(self):
        return self.user.username
