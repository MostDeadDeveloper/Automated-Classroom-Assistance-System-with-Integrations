from django.db import models
from django.conf import settings

from core.models import BaseModel

class Announcement(BaseModel):
    choices = (
        ('Weekly','Weekly',),
        ('Twice','Twice',),
        ('Minute','Minute',),
        ('Second','Second',),
        ('10Second','Second'),
    )
    frequency_type = models.CharField(max_length=20, choices=choices, blank=True, null=True)
    max_frequency = models.IntegerField(default=0) # amount of times to be repeated, if is_repetitive is TRUE
    scheduled_date = models.DateTimeField(null=True)
    content = models.CharField(max_length=75, null=True)
    is_repetitive = models.BooleanField(default=False) # determines if the announcement will be repeated
    account = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.CASCADE,
    )

