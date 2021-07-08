
from rest_framework.urlpatterns import format_suffix_patterns

from django.urls import path

from ..views.announcements import AnnoucementListAPIView

announcement_patterns = format_suffix_patterns([
    path(
        'list',
        AnnoucementListAPIView.as_view(),
        name='announcement_list',
    ),
])
