
from rest_framework.generics import ListAPIView

from ..serializers.announcements import AnnouncementSerializer

from announcement.models import Announcement


class AnnoucementListAPIView(ListAPIView):
    serializer_class = AnnouncementSerializer
    queryset = Announcement.objects.all()


class LatestAnnoucementListAPIView(ListAPIView):
    serializer_class = AnnouncementSerializer
    queryset = Announcement.objects.all()
