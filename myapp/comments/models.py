from django.db import models
from django.contrib.auth.models import User
from events.models import Event


class EventComments(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    comment_content = models.TextField()
    is_delete = models.BooleanField(default=False)
    root_comment = models.IntegerField(null=True)

    class Meta:
        db_table = 'tbl_events_comment'
