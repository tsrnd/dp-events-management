from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapp.events.serializers import UserSerializer
from django.contrib.auth.models import User
from myapp.events.models import EventMembers
from rest_framework import status


@api_view(['GET',])
def getUsers(request, id_event):
    """
    return list user invited.
    """
    RESULT_LIMIT = 40
    result_limit = int(request.GET.get('result_limit', RESULT_LIMIT))
    userList = User.objects.raw('SELECT tbl_event_members.is_going, auth_user.id, auth_user.username, auth_user.first_name, auth_user.last_name, auth_user.email, auth_user.date_joined FROM auth_user INNER JOIN tbl_event_members ON auth_user.id = tbl_event_members.user_id WHERE tbl_event_members.event_id = %s', [id_event])[:result_limit]
    serializer = UserSerializer(userList, many=True)
    content = {
        'result_count': len(userList),
        'result': serializer.data,
    }
    return Response(
        content,
        status=status.HTTP_200_OK,
    )
