from rest_framework.urlpatterns import format_suffix_patterns

from django.urls import path, include

from .account import account_patterns

app_name ='api'

urlpatterns = [
    path(
        'accounts',
        include((account_patterns,'accounts'),namespace='accounts'),
        name='account_api',
    ),
]
