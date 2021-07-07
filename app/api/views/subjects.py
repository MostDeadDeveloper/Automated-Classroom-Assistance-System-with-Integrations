from rest_framework.generics import ListAPIView

from ..serializers.subjects import SubjectScheduleSerializer

from subject.models import Subject, SubjectSchedule


class SubjectScheduleListAPIView(ListAPIView):
    serializer_class = SubjectScheduleSerializer

    def get_queryset(self, **kwargs):
        # will be another field in the future, probably discord ID
        account_id = self.kwargs.get('pk')

        return Subject.objects.filter(schedules__student__account_id=account_id)


