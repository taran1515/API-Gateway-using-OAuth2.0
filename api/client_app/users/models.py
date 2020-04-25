from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .manager import UserProfileManager


class UserProfile(AbstractUser):
    """
    Custom UserProfile Model with email as username field
    so that authentication is done using email.
    """
    username = None
    email = models.EmailField(max_length=255, unique=True,)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'password']
    objects = UserProfileManager()
    name = models.CharField(_('name'), max_length=30, blank=True)
    password = models.CharField(_('password'), max_length=128)
