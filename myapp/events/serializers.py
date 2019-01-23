from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    start_date = serializers.CharField(required=False, allow_blank=True, max_length=12)
    end_date = serializers.CharField(required=False, allow_blank=True, max_length=12)
    start_time = serializers.CharField(required=False, allow_blank=True, max_length=12)
    end_time = serializers.CharField(required=False, allow_blank=True, max_length=12)
    location = serializers.CharField(required=False, allow_blank=True, max_length=12)

    class Meta:
        model = Event
        fields = ('id', 'title', 'start_date', 'end_date', 'start_time', 'end_time', 'location')