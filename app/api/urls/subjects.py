from rest_framework.urlpatterns import format_suffix_patterns

from django.urls import path

from ..views.subjects import SubjectListAPIView

subject_patterns = format_suffix_patterns([
    path(
        'student/<int:pk>',
        SubjectListAPIView.as_view(),
        name='subject_list',
    ),
])
