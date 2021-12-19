from django.urls import path
from django.contrib.auth import views as auth_views

from location.views import LocationAddView

# from .views import CustomLoginView, SupplierDashboardView

app_name = 'location'

urlpatterns = [
    path(
        'add/',
        LocationAddView.as_view(),
        name='location_add',
    ),
    path(
        'display/',
        LocationAddView.as_view(),
        name='location_add',
    ),
]

