from rest_framework.urlpatterns import format_suffix_patterns

from django.urls import path

from ..views.account import (
    AccountListAPIView,
    ConvertDiscordIdToCredentialsAPIView,

)

account_patterns = format_suffix_patterns([
    path(
        'list',
        AccountListAPIView.as_view(),
        name='list',
    ),
    path(
        'discord/auth',
        ConvertDiscordIdToCredentialsAPIView.as_view(),
        name='discord_id_to_creds',
    ),
])
