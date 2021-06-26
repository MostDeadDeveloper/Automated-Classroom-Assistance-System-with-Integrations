from django.urls import path
from django.contrib.auth import views as auth_views

# from .views import CustomLoginView, SupplierDashboardView

app_name = 'account'

urlpatterns = [
    path(
        'user/login/',
        auth_views.LoginView.as_view(),
        {'template_name': 'account/login.html'},
        name='account_login',
    ),
    # path(
        # 'supplier/dashboard/',
        # SupplierDashboardView.as_view(),
        # name='supplier_dashboard',
    # ),
]

