from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import AccountManager

from core.models import BaseModel


class Section(BaseModel):
    year_level = models.CharField(max_length=10, null=True)
    course_code = models.CharField(max_length=16, null=True)
    couse_name = models.CharField(max_length=16, null=True)

    def __str__(self):
        return self.course_code


class Student(BaseModel):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True)
    account = models.OneToOneField(
        'account.Account',
        on_delete=models.CASCADE,
        null=True,
    )

    @property
    def full_name(self):
        return '{} - {}'.format (
            self.section,
            self.account,
        )

# Add the Professor Class Here Later
# class Professor():


class Account(AbstractUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    USERNAME_FIELD = 'email'
    username = models.CharField(
        max_length=24,
        unique=False,
        blank=True,
    )
    phone = models.CharField(
        max_length=13,
        unique=False,
        blank=True,
    )
    first_name = models.CharField(max_length=15, null=True)
    last_name = models.CharField(max_length=15, null=True)
    middle_name = models.CharField(max_length=15, null=True)

    discord_id = models.CharField(max_length=20, null=True)

    REQUIRED_FIELDS = []

    objects = AccountManager()

    def __str__(self):
        return '{} {} {} '.format(
            self.last_name,
            self.first_name,
            self.middle_name,
        )

