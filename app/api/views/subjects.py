from rest_framework.generics import ListAPIView

from ..serializers.subjects import SubjectSerializer

from subject.models import Subject


class SubjectListAPIView(ListAPIView):
    serializer_class = SubjectSerializer

    def get_queryset(self, **kwargs):
        # will be another field in the future, probably discord ID
        account_id = self.kwargs.get('pk')

        return Subject.objects.filter(schedules__student__account_id=account_id)

