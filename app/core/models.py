from django.conf import settings
from django.db import models


# Create your models here.
class BaseModel(models.Model):
    """
    Base abstract model that provides common fields
    Inherited by all of the app models

    @field
    is_active : deactivating instead of delete the record
    """
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='+',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='+',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class AppUser(BaseModel):
    """
    Base abstract model for app users that inherits 'BaseModel'
    """

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    class Meta:
        abstract = True


