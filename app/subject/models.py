from datetime import datetime, date

from django.db import models
from django.db import models
from django.conf import settings

from core.models import BaseModel
from account.models import Section


class Subject(BaseModel):
    name = models.CharField(max_length=32)
    sections = models.ManyToManyField(
        'account.Section',
    )

    def subject_subjectchedule_id(self):
        return SubjectSchedule.objects.all()


class SubjectSchedule(BaseModel):
    CHOICES = (
        ('Monday', 'Monday',),
        ('Tuesday', 'Tuesday',),
        ('Wednesday', 'Wednesday',),
        ('Thursday', 'Thursday',),
        ('Friday', 'Friday',),
        ('Saturday', 'Saturday',),
        ('Sunday', 'Sunday',),
    )
    day_of_the_week = models.CharField(max_length=16, choices=CHOICES, blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    @property
    def duration(self):
        if not (self.end_time and self.start_time):
            return 0
        end_time = datetime.combine(date.min, self.end_time)
        start_time = datetime.combine(date.min, self.start_time)
        diff = end_time - start_time

        return diff.seconds // 3600

