from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models import (
    EmailField, CharField, BooleanField, DateTimeField,
)

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = EmailField('email address', unique=True)
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    is_staff = BooleanField(default=False)
    is_active = BooleanField(default=True)
    date_joined = DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} ({self.email})'
