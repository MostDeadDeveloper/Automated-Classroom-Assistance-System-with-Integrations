from rest_framework import serializers

from subject.models import Subject, SubjectSchedule

class SubjectScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectSchedule
        fields = ('start_time','end_time',)


class SubjectSerializer(serializers.ModelSerializer):
    schedules = serializers.SerializerMethodField()

    class Meta:
        model = Subject
        fields = ('name','schedules',)

    def get_schedules(self,obj):
        schedules = SubjectSchedule.objects.filter(subject=obj)

        return SubjectScheduleSerializer(schedules, many=True).data

