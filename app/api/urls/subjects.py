from rest_framework.urlpatterns import format_suffix_patterns

from django.urls import path

from ..views.subjects import SubjectScheduleListAPIView, TodaySubjectScheduleListAPIView

subject_patterns = format_suffix_patterns([
    path(
        'student/<int:pk>',
        SubjectScheduleListAPIView.as_view(),
        name='subject_list',
    ),
    path(
        'student/<int:pk>/today',
        TodaySubjectScheduleListAPIView.as_view(),
        name='subject_list_today',
    ),
])
