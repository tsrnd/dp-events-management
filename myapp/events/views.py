from django.http import HttpResponse, JsonResponse
from .serializers import EventSerializers
from .models import Event
from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapp.events.serializers import UserSerializer
from django.contrib.auth.models import User
from myapp.events.models import EventMembers
from rest_framework import status
from django.db import connection


def index(request):
    return HttpResponse("Hello, world. You're at the event index.")


@api_view(['GET', 'DELETE'])
def event_detail(request, id_event):
    """
    GET: Get detail event by id
    DELETE: Delete event by id 
    """
    # Get event detail
    try:
        event = Event.objects.get(pk=id_event)
    except Event.DoesNotExist:
        return JsonResponse({
            "message": "Id does not exist",
            "errors": ["string"]
        },
                            status=status.HTTP_404_NOT_FOUND)

    # Hander request
    if request.method == 'GET':
        serializer = EventSerializers(event)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        if request.user.is_authenticated:
            if request.user.id == event.owner.id:
                event.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response({
                'error': "Can not delete event"
            },
                            status=status.HTTP_403_FORBIDDEN)
        return Response({
            'error': "You should be login!"
        },
                        status=status.HTTP_401_UNAUTHORIZED)


@api_view([
    'GET',
])
def getUsers(request, id_event):
    """
    return list user invited.
    """
    RESULT_LIMIT = 40
    result_limit = int(request.GET.get('result_limit', RESULT_LIMIT))
    userList = User.objects.raw(
        'SELECT tbl_event_members.is_going, auth_user.id, auth_user.username, auth_user.first_name, auth_user.last_name, auth_user.email, auth_user.date_joined FROM auth_user INNER JOIN tbl_event_members ON auth_user.id = tbl_event_members.user_id WHERE tbl_event_members.event_id = %s',
        [id_event])[:result_limit]
    serializer = UserSerializer(userList, many=True)
    content = {
        'result_count': len(userList),
        'result': serializer.data,
    }
    return Response(
        content,
        status=status.HTTP_200_OK,
    )
