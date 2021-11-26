from datetime import datetime, timedelta

import jwt
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from .managers import UserManager


class User(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def access_token(self):
        access_token_payload = {
            'user_id': self.pk,
            'exp': datetime.utcnow() + timedelta(days=0, minutes=5),
            'iat': datetime.utcnow(),
        }
        access_token = jwt.encode(access_token_payload,
                                  settings.SECRET_KEY, algorithm='HS256')
        return access_token

    @property
    def refresh_token(self):
        refresh_token_payload = {
            'user_id': self.pk,
            'exp': datetime.utcnow() + timedelta(days=7),
            'iat': datetime.utcnow()
        }
        refresh_token = jwt.encode(
            refresh_token_payload, settings.SECRET_KEY, algorithm='HS256')
        return refresh_token
