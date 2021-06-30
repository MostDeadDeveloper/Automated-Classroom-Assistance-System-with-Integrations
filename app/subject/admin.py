from django.contrib import admin

# Register your models here.

from core import admin as core_admin
from .models import Subject, SubjectSchedule

class SubjectScheduleInline(admin.TabularInline):
    model = SubjectSchedule
    fields = ('date','subject','start_time', 'end_time','duration')
    readonly_fields = ('duration',)


class SubjectAdmin(core_admin.AuditModelAdmin):
    inlines = (SubjectScheduleInline,)

admin.site.register(Subject, SubjectAdmin)
