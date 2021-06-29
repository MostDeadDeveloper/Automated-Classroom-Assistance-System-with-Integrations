from rest_framework.urlpatterns import format_suffix_patterns

from django.urls import path

from ..views.subjects import SubjectListAPIView

subject_patterns = format_suffix_patterns([
    path(
        '/list',
        SubjectListAPIView.as_view(),
        name='list',
    ),
])
