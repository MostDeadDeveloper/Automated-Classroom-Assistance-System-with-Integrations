from datetime import datetime

from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from ..serializers.subjects import SubjectScheduleSerializer

from attendance.models import Attendance, AttendanceGroup


class LogAttendanceAPIView(APIView):

    def post(self):
        account_id = self.kwargs.get('pk')
        subject_id = self.kwargs.get('subject_id')

        section = Section.objects.get(student__account_id=account_id)
        if account_id and subject_id:
            Attendance.objects.create(subj

        return pass

