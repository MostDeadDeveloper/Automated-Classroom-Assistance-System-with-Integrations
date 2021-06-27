from rest_framework.urlpatterns import format_suffix_patterns

from django.urls import path

from ..views.account import AccountListAPIView

account_patterns = format_suffix_patterns([
    path(
        '/list',
        AccountListAPIView.as_view(),
        name='list',
    ),
])
