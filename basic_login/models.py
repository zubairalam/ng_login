from django.db import models
#from django.contrib.auth import get_user_model

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import (AbstractBaseUser,
                                        BaseUserManager, PermissionsMixin)


class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        user = self.model(email=CustomUserManager.normalize_email(email), first_name=first_name, last_name=last_name, is_active=True, is_staff=True, is_superuser=False, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None, **extra_fields):
        user = self.create_user(email, first_name=first_name, last_name=last_name, password=password, **extra_fields)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True,blank=False,null=False)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    department = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(_('active status'), default=False, blank=True)
    is_staff = models.BooleanField(_('staff status'), default=False, blank=True)


    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('first_name', 'last_name')

    def get_email(self):
        return '{}'.format(self.email)

    def get_short_name(self):
        return '{}'.format(self.first_name)

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def __unicode__(self):
        return u'{}'.format(self.get_full_name())

    def __str__(self):
        return self.__unicode__()


from django.conf import settings
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
