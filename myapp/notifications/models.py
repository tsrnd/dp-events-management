from django.db import models
from django.contrib.auth.models import User


class Notification(models.Model):
    notify_link = models.TextField(null=True)
    notify_status = models.BooleanField(default=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    isDelete = models.BooleanField(default=False)

    class Meta:
        db_table = 'tbl_notifications'


class InviteMember(models.Model):
    from_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='fk_owner_invit_emember', db_column='owner')
    to_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='fk_user_id_invit_emember', db_column='user_id')
    invite_link = models.TextField(null=True)
    time_create = models.DateTimeField(null=True)
    expire_time = models.DateTimeField(null=True)
    is_confirm = models.BooleanField(default=False)
    invite_type = models.IntegerField()
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'tbl_invite_member'
