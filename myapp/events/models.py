from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateField()
    start_time = models.TimeField(null=True)
    end_date = models.DateField()
    end_time = models.TimeField(null=True)
    is_daily = models.BooleanField(default=False)
    is_all_day = models.BooleanField(default=False)
    location = models.TextField(null=True)
    is_notification = models.BooleanField(default=False)
    time_notification = models.CharField(max_length=20)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    event_content = models.TextField()
    file_attack = models.TextField()
    guest_can_invite = models.BooleanField(default=True)
    view_all_guest = models.BooleanField(default=True)
    item_preparing = models.TextField()
    is_public = models.BooleanField(default=True)
    is_cancel = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    time_create = models.DateTimeField()
    last_edit = models.DateTimeField()
    user_edit = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField()

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
    time_notification = models.CharField(max_length=20)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    event_content = models.TextField()
    file_attack = models.TextField()
    guest_can_invite = models.BooleanField(default=True)
    view_all_guest = models.BooleanField(default=True)
    item_preparing = models.TextField()
    is_public = models.BooleanField(default=True)
    is_cancel = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    time_create = models.DateTimeField()
    last_edit = models.DateTimeField()
    user_edit = models.ForeignKey(User, on_delete=models.CASCADE)
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
