from django.contrib import admin

from .models import Subject
from .models import Contact
from .models import Email
from .models import Social
from .models import Professor


admin.site.register(Subject)
admin.site.register(Contact)
admin.site.register(Email)
admin.site.register(Social)
admin.site.register(Professor)

# Register your models here.
