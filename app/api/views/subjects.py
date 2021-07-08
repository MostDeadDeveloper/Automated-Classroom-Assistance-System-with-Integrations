from datetime import datetime

from rest_framework.generics import ListAPIView

from ..serializers.subjects import SubjectScheduleSerializer

from subject.models import Subject, SubjectSchedule


class SubjectScheduleListAPIView(ListAPIView):
    serializer_class = SubjectScheduleSerializer

    def get_queryset(self, **kwargs):
        # will be another field in the future, probably discord ID
        account_id = self.kwargs.get('pk')

        return SubjectSchedule.objects.filter(section__student__account_id=account_id)


class TodaySubjectScheduleListAPIView(ListAPIView):
    serializer_class = SubjectScheduleSerializer

    def get_queryset(self, **kwargs):
        # will be another field in the future, probably discord ID
        account_id = self.kwargs.get('pk')

        week_dates = {
            0: 'Monday',
            1: 'Tuesday',
            2: 'Wednesday',
            3: 'Thursday',
            4: 'Friday',
            5: 'Saturday',
            6: 'Sunday',
        }

        return SubjectSchedule.objects.filter(
            section__student__account_id=account_id,
            day_of_the_week=week_dates[datetime.today().weekday()],
        )

