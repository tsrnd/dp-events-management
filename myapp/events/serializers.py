from rest_framework import serializers
from django.contrib.auth.models import User
from myapp.events.models import EventMembers

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