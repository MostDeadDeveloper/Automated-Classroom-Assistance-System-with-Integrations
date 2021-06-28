from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Professor
from .forms import ProfessorForm


def base_view(request):
    data_info = Professor.objects.all().order_by('professor_data')
    return render(request, 'billboard/table_view.html', {'data_info': data_info})


def info_detail(request, pk):
    data_info = get_object_or_404(Professor, pk=pk)
    return render(request, 'billboard/info_view.html', {'data_info': data_info})


def info_new(request):
    if request.method == "POST":
        form = ProfessorForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
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
            post.published_date = timezone.now()
            post.save()
            return redirect('billboard:info_detail', pk=post.pk)
    else:
        form = ProfessorForm(instance=post)
    return render(request, 'billboard/form_view.html', {'form': form})


# Create your views here.
