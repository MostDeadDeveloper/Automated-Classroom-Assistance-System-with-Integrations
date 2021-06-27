from django.urls import path
from . import views

app_name = 'billboard'

urlpatterns = [
    path('list/', views.base_view, name='base_view'),
]
