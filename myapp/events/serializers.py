from rest_framework import serializers
from myapp.events.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ("id", "start_date", "end_date", "start_time", "end_time", "is_daily", "is_all_day", "location", "is_notification", "owner", "event_content",
                  "file_attack", "guest_can_invite", "view_all_guest", "item_preparing", "is_public", "is_cancel", "is_delete", "time_create", "last_edit", "user_edit", "status")
