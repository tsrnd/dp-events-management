from rest_framework import serializers, viewsets
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import Event
from django.contrib.auth.models import User
from myapp.events.models import EventMembers


class EventSerializers(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ("id", "title", "start_date", "end_date", "start_time",
                  "end_time", "location", "time_notification", "owner",
                  "event_content", "file_attack", "guest_can_invite",
                  "view_all_guest", "item_preparing", "status", "time_create",
                  "last_edit", "user_edit")


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    date_joined = serializers.DateTimeField()
    is_going = serializers.BooleanField()


class EventMembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventMembers
        fields = ('event_id', 'user_id', 'is_going', 'is_delete', 'invite_id')
