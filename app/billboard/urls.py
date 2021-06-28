from django.urls import path
from . import views

app_name = 'billboard'

urlpatterns = [
    path('', views.base_view, name='base_view'),
    path('info/<int:pk>/', views.info_detail, name='info_detail'),
    path('info/new/', views.info_new, name='info_new'),
]
