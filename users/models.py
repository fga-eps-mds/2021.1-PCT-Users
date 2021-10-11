from django.db import models
from django.core.validators import (
    MinLengthValidator,
    MaxLengthValidator,
)

# Create your models here.

ROLE_CHOICES = (
    ('1', 'User'),
    ('2', 'Admin'),
)

class User(models.Model):
    name = models.CharField(
        max_length=240,
        blank=False,
        null=False
    )
    email = models.EmailField(
        max_length=240,
        unique=True,
        blank=False,
        null=False
    )
    password = models.CharField(
        max_length=240,
        blank=False,
        null=False
    )
    roleId = models.CharField(
        default=1,
        max_length=1,
        null=False,
        blank=False,
        choices=ROLE_CHOICES,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(1)
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name