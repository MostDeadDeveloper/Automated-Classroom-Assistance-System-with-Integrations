from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.shortcuts import render, redirect, reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    FormView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.views.generic import View


class GenericView(View):
    """Base view that every view should inherit from.

    Adds a default `user` instance to the context data

    """
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = {}
        context.update(**kwargs)
        return context

    def get(self, request, *args,  **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)


class LoginGenericView(LoginRequiredMixin, GenericView):
    """Any core view that requires a login redirect should inherit from.

    """
    login_url = 'login'


class LoginDetailView(LoginRequiredMixin, DetailView):
    login_url = 'login'

    def get_context_data(self, **kwargs):
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)
        context.update(**kwargs)
        context.update(self.kwargs)

        return context

    def get(self, request, *args, **kwargs):
        return super().get(request, **kwargs)


class LoginFormView(LoginRequiredMixin, FormView):
    """Any core view that requires a login redirect should inherit from.

    """
    login_url = 'login'


class LoginListView(LoginRequiredMixin, ListView):
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(**kwargs)
        context.update(self.kwargs)

        return context

    def get(self, request, *args, **kwargs):
        return super().get(request, **kwargs)


class LoginCreateView(LoginRequiredMixin, CreateView):
    """Any core view that requires a login redirect should inherit from.

    """
    login_url = 'account_login'

class LoginUpdateView(LoginRequiredMixin, UpdateView):
    """Any core view that requires a login redirect should inherit from.

    """
    login_url = 'account_login'


class LoginDeleteView(LoginRequiredMixin, DeleteView):
    """Any core view that requires a login redirect should inherit from.

    """
    login_url = 'account_login'

