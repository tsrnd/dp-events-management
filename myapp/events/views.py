from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from .serializers import EventSerializer
from .models import Event
from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapp.events.serializers import UserSerializer
from django.contrib.auth.models import User
from myapp.events.models import EventMembers
from rest_framework import status
from rest_framework.parsers import FormParser
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

RESULT_LIMIT = 5
IS_PUBLIC = True


def index(request):
    return HttpResponse("Hello, world. You're at the event index.")


class EventList(APIView):
    """
    List all events.
    """

    def get(self, request, format=None):
        public = request.GET.get("is_public", IS_PUBLIC)
        owner = request.GET.get('owner', False)
        start_date = request.GET.get('start_date', False)
        end_date = request.GET.get('end_date', False)
        status = request.GET.get('status', False)
        event_list = Event.objects.all().filter(is_public=public)
        order = request.GET.get('order', 'id')
        event_list = event_list.order_by(order)
        if owner:
            event_list = event_list.filter(owner=owner)
        if start_date:
            event_list = event_list.filter(start_date=start_date)
        if end_date:
            event_list = event_list.filter(end_date=end_date)
        if status:
            event_list = event_list.filter(status=status)
        page = request.GET.get('page', 1)
        result_limit = request.GET.get("result_limit", RESULT_LIMIT)
        paginator = Paginator(event_list, result_limit)
        try:
            events = paginator.page(page)
        except PageNotAnInteger as pniErr:
            events = paginator.page(1)
        except EmptyPage as epErr:
            events = paginator.page(paginator.num_pages)
        serializer = EventSerializer(events, many=True)
        content = {
            'result_count': event_list.count(),
            'page': events.number,
            'next_page_flg': events.has_next(),
            'result': serializer.data,
        }
        return Response(content)


@api_view(['GET', 'PUT'])
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
        serializer = EventSerializer(event)
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
    elif request.method == 'PUT':
        if request.user.is_authenticated:
            if request.user.id == event.owner.id:
                data = FormParser().parse(request)
                for key, value in data.items():
                    setattr(event, key, value)
                event.save()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response({
                    'error': "Can not edit event"
                },
                                status=status.HTTP_403_FORBIDDEN)
        else:
            return Response({
                'error': "Please login!"
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
