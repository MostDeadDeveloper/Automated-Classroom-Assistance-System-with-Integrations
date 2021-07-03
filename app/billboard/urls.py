from django.urls import path
from . import views

from billboard.views import BaseView, InfoDetailView

app_name = 'billboard'

urlpatterns = [
    path(
        '',
        BaseView.as_view(),
        name='base_view'
    ),
    path(
        'info/<int:pk>/',
         InfoDetailView.as_view(),
         name='info_detail'
    ),
    path(
        'info/new/',
        views.info_new,
        name='info_new'
    ),
    path(
        'info/<int:pk>/edit/',
        views.info_edit,
        name='info_edit'
    ),
    path(
        'info/<pk>/remove/',
        views.info_remove,
        name='info_remove'
    ),
]
