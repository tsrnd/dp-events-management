from rest_framework import serializers
from myapp.events.models import Event


class EventSerializer(serializers.ModelSerializer):
    def validate(self, data):
        """
        Check whether start date greater end date.
        """
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError("end date should be greater than start date.")
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
