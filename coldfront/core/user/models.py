from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):

    """ Displays a user's profile. A user can be a principal investigator (PI), administrator, or center director. The is_pi field indicates whether or not a user is a PI. """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_pi = models.BooleanField(default=False)