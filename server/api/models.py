from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils import timezone

# Create your models here.
from server.api.managers import CustomUserManager


class Role(models.Model):
    name = models.CharField(max_length=30, blank=False, unique=True)

    class Meta:
        db_table = 'roles'


class AuthUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        'username',
        max_length=150,
        unique=True,
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        validators=[UnicodeUsernameValidator()],
        error_messages={
            'unique': 'A user with that username already exists.',
        },
    )
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    email = models.EmailField(unique=True, blank=False)
    phone = models.CharField(max_length=16, blank=False, unique=True)
    date_joined = models.DateTimeField(default=timezone.now)
    address = models.CharField(max_length=60, blank=True, null=True)
    role = models.ForeignKey(Role, on_delete=models.DO_NOTHING, default=1)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'auth_user'


class Category(models.Model):
    name = models.CharField(max_length=40, blank=False, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        db_table = 'category'


class DangerLevel(models.Model):
    name = models.CharField(max_length=15, blank=False, unique=True)

    class Meta:
        db_table = 'danger_level'

