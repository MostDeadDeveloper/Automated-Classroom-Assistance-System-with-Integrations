from django.shortcuts import render
from django.views.generic.base import RedirectView
from django.urls import reverse

from core.views import LoginGenericView, GenericView, LoginListView

# Create your views here.

class BaseRedirectView(RedirectView):

    def get_redirect_url(self, **kwargs):
        user = self.request.user

        if not user.is_authenticated:
            return reverse('account:account_login')

        if user.is_authenticated:
            return reverse('account:dashboard')

        # if user.is_bidder:
            # return reverse('products:all_products_bidded')


class DashboardView(LoginGenericView):
    template_name = 'account/dashboard.html'


