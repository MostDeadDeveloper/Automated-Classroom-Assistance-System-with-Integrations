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
            return reverse('subject:account_login')

        if user.is_authenticated:
            return reverse('subject:schedule_view')

        # if user.is_bidder:
        #     return reverse('products:all_products_bidded')


class ScheduleView(LoginGenericView):

    template_name = 'subject/schedule_view.html'

    def get_context_data(self, **kwargs):
        current_user = self.request.user

        context = super().get_context_data(**kwargs)

        student_account_id = Student.objects.get(account_id=current_user.id)
        # context['student_data'] = Student.objects.get(account_id=current_user.id)
        context['section_data'] = Section.objects.get(id=student_account_id.section_id)

        # context['subject_data'] = Subject.objects.filter(sections__student__section_id=student_account_id.section_id)
        context['subject_data'] = Subject.objects.filter(sections__student__section_id=student_account_id.section_id)
        context['subject_data'] = SubjectSchedule.objects.filter(id=context['subject_data'])

        # context['subject_data'] = Subject.objects.get(ss=student_account_id.section_id)
        # context['subject_data'] = SubjectSchedule.objects.get(section_id=student_account_id.section_id)
        # context['subject_data'] = Section.objects.get(section_id=student_account_id.section_id)
        # context['subjectschedule_data'] = SubjectSchedule.objects.order_by('day_of_the_week')
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
