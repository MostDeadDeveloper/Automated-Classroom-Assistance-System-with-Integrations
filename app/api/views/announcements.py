
from rest_framework.generics import ListAPIView, CreateAPIView

from ..serializers.announcements import AnnouncementSerializer, NoteSerializer

from announcement.models import Announcement, Note


class AnnoucementListAPIView(ListAPIView):
    serializer_class = AnnouncementSerializer
    queryset = Announcement.objects.all()


class LatestAnnoucementListAPIView(ListAPIView):
    serializer_class = AnnouncementSerializer

    def get_queryset(self, **kwargs):
        account_id = self.kwargs.get('pk')
        count = self.kwargs.get('counter')

        return Announcement.objects.filter(
            section__student__account_id=account_id,
        ).order_by('scheduled_date')[0:count]


class LatestNotesListAPIView(ListAPIView):
    serializer_class = NoteSerializer

    def get_queryset(self, **kwargs):
        account_id = self.kwargs.get('pk')
        count = self.kwargs.get('counter')
        subject_id = self.kwargs.get('subject_id')

        return Note.objects.filter(
            account_id=account_id,
            subject_id=subject_id,
        ).order_by('created_time')[0:count]

class CreateNoteListAPIView(ListAPIView):
    serializer_class = NoteSerializer
