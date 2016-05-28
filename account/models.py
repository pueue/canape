from django.db import models
from django.contrib.auth.models import (
        BaseUserManager,
        AbstractBaseUser,
        PermissionsMixin
)

class UserManager(BaseUserManager):
    def create_user(self, email, username, password, **kwargs):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
                email=self.normalize_email(email),
                username=username,
                is_active=True,
                **kwargs
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password, **kwargs):
        user = self.model(
                    email=self.normalize_email(email),
                    username=username,
                    is_staff=True,
                    is_superuser=True,
                    is_active=True,
                    **kwargs
        )
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
                max_length=254,
                unique=True,
    )
    username = models.CharField(
                max_length=20,
                unique=True,
    )
    image = models.ImageField(
                upload_to='image/profile/',
    )

    description = models.TextField()
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def get_full_name(self):
        return self.email
    def get_short_name(self):
        return self.email
