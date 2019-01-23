from django.http import HttpResponse
from .models import Event
from .serializers import EventSerializer
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status, mixins, generics
import sys

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the event index.")

class PublicEventList(mixins.ListModelMixin, mixins.CreateModelMixin,
                  generics.GenericAPIView):
    def get_queryset(self):
        request = self.request
        public = True
        qr = Event.objects.filter(is_public = public)
        if request.GET.get('is_public'):
            public = request.GET.get('is_public') == 'TRUE'
        status = request.GET.get('status')
        if status is not None and status.isnumeric():
            qr = qr.filter(status = int(status))
        if request.GET.get('start_date') is not None:
            qr = qr.filter(start_date = request.GET.get('start_date'))
        if request.GET.get('end_date') is not None:
            qr = qr.filter(end_date = request.GET.get('end_date'))
        return qr
    serializer_class = EventSerializer
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        resultLimit = 10
        page = 1
        result_limit = request.GET.get('result_limit')
        if result_limit is not None and result_limit.isnumeric():
            resultLimit = int(result_limit)
        pg = request.GET.get('page')
        if pg is not None and pg.isnumeric():
            page = int(pg)
        nextPageFlg = queryset.count() > resultLimit*page
        serializer = EventSerializer(list(queryset[(page - 1)*resultLimit:resultLimit*page]), many=True)
        content = {
            'result_count': queryset.count(),
            'page': page,
            'event_list': serializer.data,
            'next_page_flg': nextPageFlg
        }
        return Response(content)