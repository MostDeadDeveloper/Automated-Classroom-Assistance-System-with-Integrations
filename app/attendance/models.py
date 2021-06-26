from django.db import models
from django.conf import settings

from core.models import BaseModel

class Attendance(BaseModel):
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    account = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.CASCADE,
    )

