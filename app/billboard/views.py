from django.shortcuts import render
from django.utils import timezone
from .models import Professor
from .models import Subject
from .models import Contact
from .models import Email
from .models import Social


def base_view(request):
    professor_data = Professor.objects.all().order_by('professor_in')
    subject_data = Subject.objects.all()
    contact_data = Contact.objects.all()
    email_data = Email.objects.all()
    social_data = Social.objects.all()
    data_info = {
        'professor_data': professor_data,
        'subject_data': subject_data,
        'contact_data': contact_data,
        'email_data': email_data,
        'social_data': social_data
    }
    return render(request, 'billboard/table_view.html', data_info)

# def base_view(request):
    # professor_data = Professor.objects.all().order_by('subject_out')
    # subject_data = Subject.objects.all()
    # data_info = {'professor_data': professor_data, 'subject_data': subject_data}
    # return render(request, 'billboard/table_view.html', data_info=data_info)

# Create your views here.
