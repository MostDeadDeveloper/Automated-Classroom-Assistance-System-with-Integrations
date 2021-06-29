from django.db import models
from django.db import models
from django.conf import settings

from core.models import BaseModel

class Subject(BaseModel):
    name = models.CharField(max_length=32)
    duration = models.IntegerField(default=0)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)


