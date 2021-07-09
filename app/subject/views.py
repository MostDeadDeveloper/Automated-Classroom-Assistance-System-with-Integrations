from django.shortcuts import render
from django.views.generic.base import RedirectView
from django.urls import reverse

from account.models import Student, Section
from .models import Subject, SubjectSchedule

from core.views import LoginGenericView


class BaseRedirectView(RedirectView):
    def get_redirect_url(self, **kwargs):
        user = self.request.user

        if not user.is_authenticated:
            return reverse('account:account_login')

        if user.is_authenticated:
            return reverse('subject:schedule_view')


class ScheduleView(LoginGenericView):

    template_name = 'subject/schedule_view.html'

    def get_context_data(self, **kwargs):
        current_user = self.request.user

        context = super().get_context_data(**kwargs)

        student_account_id = Student.objects.get(account_id=current_user.id)
        context['section_data'] = Section.objects.get(id=student_account_id.section_id)

        context['schedule_data'] = SubjectSchedule.objects.filter(section_id=student_account_id.section_id).order_by('start_time')
        return context


# class ScheduleView(LoginGenericView):
#     # model = Subject
#     template_name = 'subject/schedule_view.html'
#     # context_object_name = 'subject_data'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['subject_data'] = Subject.objects.order_by('sections')
#         context['subjectschedule_data'] = SubjectSchedule.objects.order_by('day_of_the_week')
#         return context

# Create your views here.
