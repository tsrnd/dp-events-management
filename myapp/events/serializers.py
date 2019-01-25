from rest_framework import serializers
from myapp.events.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            "id",
            "title",
            "start_date",
            "end_date",
            "start_time",
            "end_time",
            "is_daily",
            "is_all_day",
            "location",
            "is_notification",
            "event_content",
            "file_attack",
            "guest_can_invite",
            "view_all_guest",
            "item_preparing",
            "is_public",
            "is_cancel",
            "status",
        )
