from django.urls import path
from django.contrib.auth import views as auth_views

from account.views import DashboardView

# from .views import CustomLoginView, SupplierDashboardView

app_name = 'account'

urlpatterns = [
    path(
        'user/login/',
        auth_views.LoginView.as_view(),
        {'template_name': 'account/login.html'},
        name='account_login',
    ),
    path(
        'user/dashboard/',
        DashboardView.as_view(),
        name='dashboard',
    ),
    # path(
        # 'supplier/dashboard/',
        # SupplierDashboardView.as_view(),
        # name='supplier_dashboard',
    # ),
]

