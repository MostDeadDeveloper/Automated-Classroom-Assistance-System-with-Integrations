from django.contrib import admin

from .models import Attendance, AttendanceGroup

from core import admin as core_admin


class AttendanceInline(admin.TabularInline):
    model = Attendance
    fields = ('start_date','end_date','account',)


class AttendanceGroupAdmin(core_admin.AuditModelAdmin):
    inlines = (AttendanceInline,)

admin.site.register(Attendance)
admin.site.register(AttendanceGroup, AttendanceGroupAdmin)

# Register your models here.
