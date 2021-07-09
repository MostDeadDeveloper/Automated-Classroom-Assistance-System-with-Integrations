from rest_framework import serializers

from subject.models import Subject, SubjectSchedule

class SubjectScheduleSerializer(serializers.ModelSerializer):
    subject = serializers.CharField(source='subject.name',read_only=True)
    subject_id = serializers.CharField(source='subject.id',read_only=True)

    class Meta:
        model = SubjectSchedule
        fields = ('start_time','end_time','subject', 'subject_id')


class SubjectSerializer(serializers.ModelSerializer):
    schedules = serializers.SerializerMethodField()

    class Meta:
        model = Subject
        fields = ('name','schedules',)

    def get_schedules(self,obj):
        schedules = SubjectSchedule.objects.filter(subject=obj)

        return SubjectScheduleSerializer(schedules, many=True).data

