from django.shortcuts import render

from core.views import LoginGenericView, GenericView, LoginListView

# Create your views here.

class LocationAddView(LoginGenericView):
    template_name = 'location/add_location.html'

class LocationAddView(LoginGenericView):
    template_name = 'location/display_location.html'
