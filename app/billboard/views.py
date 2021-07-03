from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views.generic.base import RedirectView
from django.utils import timezone

from .models import Professor
from .forms import ProfessorForm

from core.views import LoginGenericView


class BaseRedirectView(RedirectView):
    def get_redirect_url(self, **kwargs):
        user = self.request.user

        if not user.is_authenticated:
            return reverse('account:account_login')

        if user.is_authenticated:
            return reverse('billboard:base_view')


class BaseView(LoginGenericView):

    template_name = 'billboard/table_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data_info'] = Professor.objects.all().order_by('professor_data')
        return context


class InfoDetailView(LoginGenericView):

    template_name = 'billboard/info_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data_info'] = get_object_or_404(Professor, pk=self.kwargs["pk"])
        return context



def info_new(request):
    if request.method == "POST":
        form = ProfessorForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.up_date = timezone.now()
            post.save()
            return redirect('billboard:info_detail', pk=post.pk)
    else:
        form = ProfessorForm()
    return render(request, 'billboard/form_view.html', {'form': form})


def info_edit(request, pk):
    post = get_object_or_404(Professor, pk=pk)
    if request.method == "POST":
        form = ProfessorForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.up_date = timezone.now()
            post.save()
            return redirect('billboard:info_detail', pk=post.pk)
    else:
        form = ProfessorForm(instance=post)
    return render(request, 'billboard/form_view.html', {'form': form})


def info_remove(request, pk):
    post = get_object_or_404(Professor, pk=pk)
    post.delete()
    return redirect('billboard:base_view')


# Create your views here.
