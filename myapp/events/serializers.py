from rest_framework import serializers, viewsets
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import Event


class EventSerializers(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ("title",
                  "start_date",
                  "end_date",
                  "start_time",
                  "end_time",
                  "location",
                  "time_notification",
                  "owner",
                  "event_content",
                  "file_attack",
                  "guest_can_invite",
                  "view_all_guest",
                  "item_preparing",
                  "status",
                  "time_create",
                  "last_edit",
                  "user_edit")
