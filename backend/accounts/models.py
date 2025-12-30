from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from .manager import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    EMPLOYER = 'EMPLOYER'
    SEEKER = 'SEEKER'

    ROLE_CHOICES = [
        (EMPLOYER, 'Employer'),
        (SEEKER, 'Seeker'),
    ]

    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'role']

    objects = UserManager()

    def __str__(self):
        return self.email
