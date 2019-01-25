from django.http import HttpResponse
from myapp.events.models import Event
from myapp.events.serializers import EventSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

RESULT_LIMIT = 5
IS_PUBLIC = True

# Create your views here.


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
            events = paginator.num_pages
        serializer = EventSerializer(events, many=True)
        content = {
            'result_count': event_list.count(),
            'page': page,
            'next_page_flg': events.has_next(),
            'result': serializer.data,
        }
        return Response(content)
