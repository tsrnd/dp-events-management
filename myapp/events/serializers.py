from rest_framework import serializers
from myapp.events.models import Event
from datetime import date


class EventSerializer(serializers.ModelSerializer):
    def validate(self, data):
        """
        Check conditions date and time (start, end).
        """
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError({"end_date":"end date should be greater than start date."})
        elif data['start_date'] == data['end_date']:
            if data['start_time'] >= data['end_time']:
                raise serializers.ValidationError({"end_time":"end time should be greater than start time."})
        today = date.today()
        if data['start_date'] < today:
            raise serializers.ValidationError({"start_date":"start date should be greater than today."})

        # check validator title, start date and end date is exist
        if Event.custom_objects.is_exist(data["title"], data['start_date'], data['end_date']):
            raise serializers.ValidationError({"event":"This Event has already existed"})

        return data

    class Meta:
        model = Event
        fields = (
            'id',
            'title',
            'start_date',
            'start_time',
            'end_date',
            'end_time',
            'is_daily',
            'is_all_day',
            'location',
            'owner',
            'is_notification',
            'time_notification',
            'event_content',
            'file_attack',
            'guest_can_invite',
            'view_all_guest',
            'item_preparing',
            'is_public',
            'is_cancel',
            'is_delete',
            'time_create',
            'last_edit',
            'user_edit',
            'status',
        )
