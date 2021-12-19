from django.db import models
from django.conf import settings

from core.models import BaseModel

class Attendance(BaseModel):
    start_date = models.TimeField(null=True)
    end_date = models.TimeField(null=True)
    account = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.CASCADE,
    )
    attendance_group = models.ForeignKey(
        'attendance.AttendanceGroup',
        on_delete=models.CASCADE,
        null=True,
    )


class AttendanceGroup(BaseModel):
    section = models.ForeignKey(
        'account.Section',
        on_delete=models.CASCADE,
        null=True,
    )
    subject_sched = models.ForeignKey(
        'subject.SubjectSchedule',
        on_delete=models.CASCADE,
        null=True,
    )
    duration = models.IntegerField(default=0)
    repetition = models.IntegerField(default=0)

    def __str__(self):
        return '{} - {}'.format(self.section.name, self.subject_sched)
