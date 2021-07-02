from django.urls import path
from django.contrib.auth import views as auth_views

from subject.views import ScheduleView

app_name = 'subject'

urlpatterns = [
    path(
        'schedule/',
        ScheduleView.as_view(),
        name='schedule_view'
        ),
]
