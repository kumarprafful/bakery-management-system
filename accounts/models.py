from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserManager(BaseUserManager):
    def _create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError('Email is required')

        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user
    
    def create_user(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', False)
        kwargs.setdefault('is_superuser', False)
        kwargs.setdefault('is_active', True)
        return self._create_user(email, password, **kwargs)

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)
        
        if kwargs.get('is_staff') is not True:
            raise ValueError('superuser must be a staff')
        if kwargs.get('is_superuser') is not True:
            raise ValueError('superuser must be superuser')

        return self._create_user(email, password, **kwargs)

class User(AbstractBaseUser, PermissionsMixin):
    USER_ROLE_CHOICES = (
        (1, 'admin'),
        (2, 'customer'),
    )

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    email = models.EmailField(unique=True)
    
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)

    user_role = models.IntegerField(choices=USER_ROLE_CHOICES, default=2)
    
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email
    
    @property
    def full_name(self):
        if self.first_name:
            return '{} {}'.format(self.first_name if self.first_name else '', self.last_name if self.last_name else '')
        else:
            return None

