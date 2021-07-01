from django.contrib import admin

from core import admin as core_admin
from .models import Account, Student, Section


class StudentInline(admin.TabularInline):
    model = Student
    fields = ('full_name','account',)
    readonly_fields = ('full_name',)


class SectionAdmin(core_admin.AuditModelAdmin):
    inlines = (StudentInline,)

admin.site.register(Account)
admin.site.register(Section, SectionAdmin)
admin.site.register(Student)


