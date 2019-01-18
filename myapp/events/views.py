from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from myapp.events.serializers import EventSerializer
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return HttpResponse("Hello, world. You're at the event index.")

@csrf_exempt
def create(request):
    """
        Create a new Event
    """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EventSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
