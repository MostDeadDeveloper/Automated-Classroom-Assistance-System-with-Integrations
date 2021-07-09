from datetime import datetime, date

from django.db import models
from django.db import models
from django.conf import settings

from core.models import BaseModel
from account.models import Section


class Subject(BaseModel):
    name = models.CharField(max_length=32)
    schedules = models.ManyToManyField(
        'account.Section',
        through='SubjectSchedule',
        through_fields=('subject', 'section'),
    )

    def subject_subjectschedule_id(self):
        return SubjectSchedule.objects.all()

    def __str__(self):
        return self.name

class SubjectSchedule(BaseModel):
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        null=True
    )
    section = models.ForeignKey(
        'account.Section',
        on_delete=models.CASCADE,
        null=True,
    )

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

    @property
    def duration(self):
        if not (self.end_time and self.start_time):
            return 0
        end_time = datetime.combine(date.min, self.end_time)
        start_time = datetime.combine(date.min, self.start_time)
        diff = end_time - start_time

        return diff.seconds // 3600

    def __str__(self):
        return '{} - {} {} -  {}'.format(self.subject, self.section, self.start_time, self.end_time)

