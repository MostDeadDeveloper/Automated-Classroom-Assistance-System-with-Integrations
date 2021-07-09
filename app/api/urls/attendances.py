from rest_framework.urlpatterns import format_suffix_patterns

from django.urls import path

from ..views.attendances import LogAttendanceAPIView

subject_patterns = format_suffix_patterns([
    path(
        'student/<int:pk>/subject/<int:subject_id>',
        LogAttendanceAPIView.as_view(),
        name='log_attendance',
    ),
])
