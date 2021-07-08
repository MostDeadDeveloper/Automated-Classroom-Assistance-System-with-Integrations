
from rest_framework.generics import ListAPIView

from ..serializers.announcements import AnnouncementSerializer

from announcement.models import Announcement


class AnnoucementListAPIView(ListAPIView):
    serializer_class = AnnouncementSerializer
    queryset = Announcement.objects.all()


class LatestAnnoucementListAPIView(ListAPIView):
    serializer_class = AnnouncementSerializer

    def get_queryset(self, **kwargs):
        account_id = self.kwargs.get('pk')
        count = self.kwargs.get('counter')

        return Announcement.objects.filter(
            account=account_id,
        ).order_by('scheduled_date')[0:count]
