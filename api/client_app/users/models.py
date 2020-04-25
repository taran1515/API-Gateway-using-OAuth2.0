from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .UserProfileManager import UserProfileManager


class UserProfile(AbstractUser):

    username = None
    email =  models.EmailField(max_length=255,unique=True,)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','password']


    objects = UserProfileManager()
    name = models.CharField(_('name'), max_length=30, blank=True)
    password = models.CharField(_('password'), max_length=128)
    

#     # objects = UserManager()
    
#     # REQUIRED_FIELDS = []