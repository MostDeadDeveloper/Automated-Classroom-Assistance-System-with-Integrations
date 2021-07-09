from django.contrib import admin

from .models import Attendance, AttendanceGroup


admin.site.register(Attendance)
admin.site.register(AttendanceGroup)

# Register your models here.
