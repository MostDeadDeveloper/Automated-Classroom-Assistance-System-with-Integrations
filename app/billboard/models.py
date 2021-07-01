from django.db import models
from django.conf import settings
from django.utils import timezone
from django.shortcuts import redirect


class Professor(models.Model):
    professor_data = models.CharField(max_length=100)
    subject_data = models.TextField(max_length=300, blank=True)
    contact_data = models.TextField(max_length=300, blank=True)
    email_data = models.TextField(max_length=300, blank=True)
    social_data = models.TextField(max_length=300, blank=True)
    up_date = models.DateField(blank=True, null=True)

    def publish(self):
        self.up_dates = timezone.now()
        self.save()

    def __str__(self):
        return self.professor_data

# Create your models here.
