from django.db import models
from django.conf import settings
from django.utils import timezone


class Subject(models.Model):
    subject_in = models.CharField(max_length=100)

    def __str__(self):
        return self.subject_in


class Contact(models.Model):
    contact_in = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.contact_in


class Email(models.Model):
    email_in = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.email_in


class Social(models.Model):
    social_in = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.social_in


class Professor(models.Model):
    professor_in = models.CharField(max_length=100)
    subject_out = models.ManyToManyField(Subject, blank=True)
    contact_out = models.ManyToManyField(Contact, blank=True)
    email_out = models.ManyToManyField(Email, blank=True)
    social_out = models.ManyToManyField(Social, blank=True)
    up_date = models.DateField(blank=True, null=True)

    def publish(self):
        self.up_dates = timezone.now()
        self.save()

    def __str__(self):
        return self.professor_in

# Create your models here.
