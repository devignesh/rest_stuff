from django.db import models    
from django.utils import timezone
from django.contrib.auth.models import UserManager
from django.contrib.auth import get_user_model
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin 
)

# Create your models here.

class Myuser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True,max_length=254)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    mobile = models.IntegerField(unique=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'mobile']

class Message(models.Model):
    msg = models.CharField(max_length=50)


class EmailOrMobileAuthBackend(object):
    def authenticate(self, email=None, password=None):
        try:
            user = get_user_model().objects.get(email=username)
            if user.check_password(password):
                return user
        except user.DoesNotExist:
            if username.isdigit():
                try:
                    user = get_user_model().objects.get(mobile=username)
                    if user.check_password(password):
                        return user
                except user.DoesNotExist:
                    return None
            else:
                return None

        def get_user(self, user_id):
            try:
                return get_user_model().objects.get(pk=user_id)
            except user.DoesNotExist:
                return None