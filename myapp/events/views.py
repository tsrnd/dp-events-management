from rest_framework.parsers import FormParser
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from myapp.events.serializers import UserSerializer
from myapp.events.serializers import EventSerializer

from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from myapp.events.models import Event
from myapp.events.models import EventMembers


@api_view(['POST'])
def index(request):
    """
        Create a new Event
    """
    if request.method == 'POST':
        data = FormParser().parse(request)
        serializer = EventSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def event_detail(request, id_event):
    """
    Get The detail event by id
    """
    try:
        event = Event.objects.get(pk=id_event)
    except:
        return JsonResponse({
            "message": "ID does not exist",
            "errors": ["string"]
        },
                            status=status.HTTP_302_FOUND)

    if request.method == 'GET':
        serializer = EventSerializer(event)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
    else:
        return JsonResponse({
            "message": "Request Forbiden",
            "errors": ["string"]
        },
        status=status.HTTP_403_FORBIDDEN)


@api_view(['GET',])
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
