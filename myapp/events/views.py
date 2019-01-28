from django.http import HttpResponse, JsonResponse
from .serializers import EventSerializers
from .models import Event
from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapp.events.serializers import UserSerializer
from django.contrib.auth.models import User
from myapp.events.models import EventMembers
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.db import connection


def index(request):
    return HttpResponse("Hello, world. You're at the event index.")


@api_view(['GET', 'DELETE'])
def event_detail(request, id_event):
    """
    GET: Get detail event by id
    DELETE: Delete event by id 
        Request Paramater:
        {
            "token" : "abcxyz"
        }
    """

    #get authorization
    authorization = str(request.META.get('HTTP_AUTHORIZATION'))
    try:
        token = authorization.split(' ')[1]
    except IndexError:
        return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

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
        cursor = connection.cursor()
        sql = "SELECT count(*) FROM tbl_events AS e INNER JOIN authtoken_token AS aut ON e.owner = aut.user_id WHERE e.id={} AND aut.key='{}'".format(
            id_event, token)
        cursor.execute(sql)
        row = cursor.fetchone()[0]
        if row == 1:
            event.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)


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
