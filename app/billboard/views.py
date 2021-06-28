from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Professor
from .forms import ProfessorPostForm


def base_view(request):
    professor_data = Professor.objects.all().order_by('professor_in')
    return render(request, 'billboard/table_view.html', {'professor_data': professor_data})


def info_detail(request, pk):
    # Professor.objects.get(pk=pk)
    professor_data = get_object_or_404(Professor, pk=pk)
    return render(request, 'billboard/info_view.html', {'professor_data': professor_data})


def info_new(request):
    form = ProfessorPostForm()
    return render(request, 'billboard/form_view.html', {'form': form})

# def base_view(request):
    # professor_data = Professor.objects.all().order_by('subject_out')
    # subject_data = Subject.objects.all()
    # data_info = {'professor_data': professor_data, 'subject_data': subject_data}
    # return render(request, 'billboard/table_view.html', data_info=data_info)

# Create your views here.
