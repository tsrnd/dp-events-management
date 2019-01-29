from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class EventValidator(models.Manager):
    def is_exist(self, title, start_date, end_date):
        try:
            _ = Event.objects.get(title=title, start_date=start_date, end_date=end_date)
            return True
        except Event.DoesNotExist:
            return False

class Event(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateField()
    start_time = models.TimeField(null=True)
    end_date = models.DateField()
    end_time = models.TimeField(null=True)
    is_daily = models.BooleanField(default=False)
    is_all_day = models.BooleanField(default=False)
    location = models.TextField()
    is_notification = models.BooleanField(default=False)
    time_notification = models.CharField(max_length=20, null=True)
    owner = models.IntegerField(null=True)
    event_content = models.TextField(null=True)
    file_attack = models.TextField(null=True)
    guest_can_invite = models.BooleanField(default=True)
    view_all_guest = models.BooleanField(default=True)
    item_preparing = models.TextField(null=True)
    is_public = models.BooleanField(default=True)
    is_cancel = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    time_create = models.DateTimeField(auto_now_add=True)
    last_edit = models.DateTimeField(auto_now=True)
    user_edit = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='fk_user_edit_event', db_column='user_edit', null=True)
    status = models.IntegerField(null=True)

    objects = models.Manager()
    custom_objects = EventValidator()
    class Meta:
        db_table = 'tbl_events'


class EventHistory(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateField()
    start_time = models.TimeField(null=True)
    end_date = models.DateField()
    end_time = models.TimeField(null=True)
    is_daily = models.BooleanField(default=False)
    is_all_day = models.BooleanField(default=False)
    location = models.TextField(null=True)
    is_notification = models.BooleanField(default=False)
    time_notification = models.CharField(max_length=20, null=True)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='fk_owner_event_history', db_column='owner')
    event_content = models.TextField(null=True)
    file_attack = models.TextField(null=True)
    guest_can_invite = models.BooleanField(default=True)
    view_all_guest = models.BooleanField(default=True)
    item_preparing = models.TextField(null=True)
    is_public = models.BooleanField(default=True)
    is_cancel = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    time_create = models.DateTimeField()
    last_edit = models.DateTimeField()
    user_edit = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='fk_user_edit_event_history', db_column='user_edit')
    eventId = models.ForeignKey(Event, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tbl_events_history'


class EventMembers(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    is_going = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    invite_id = models.IntegerField(null=True)

    class Meta:
        db_table = 'tbl_event_members'
