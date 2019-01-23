from rest_framework import serializers
from .models import Event
from .models import User

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = User
        fields = ('id')

class EventSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    start_date = serializers.CharField(required=False, allow_blank=True, max_length=12)
    end_date = serializers.CharField(required=False, allow_blank=True, max_length=12)
    start_time = serializers.CharField(required=False, allow_blank=True, max_length=12)
    end_time = serializers.CharField(required=False, allow_blank=True, max_length=12)
    location = serializers.CharField(required=False, allow_blank=True, max_length=12)
    time_notication = serializers.CharField(required=False, allow_blank=True, max_length=20)
    owner = serializers.SerializerMethodField()
    event_content = serializers.CharField(max_length=100)
    file_attack = serializers.CharField(max_length=100)
    guest_can_invite = serializers.BooleanField()
    view_all_guest = serializers.BooleanField()
    item_preparing = serializers.CharField(max_length=100)
    status = serializers.IntegerField()
    time_create = serializers.CharField(max_length=20)
    user_edit = serializers.SerializerMethodField()
    last_edit = serializers.CharField(max_length=20)

    class Meta:
        model = Event
        fields = ('id', 'title', 'start_date', 'end_date', 'start_time', 'end_time', 'location', 'owner')
    
    def get_owner(self, obj):
        return obj.owner.id
    def get_user_edit(self, obj):
        return obj.user_edit.id

    
