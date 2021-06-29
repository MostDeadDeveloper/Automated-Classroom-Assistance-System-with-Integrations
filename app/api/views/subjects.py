from rest_framework.generics import ListAPIView

from ..serializers.subjects import SubjectSerializer

from subject.models import Subject


class SubjectListAPIView(ListAPIView):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
