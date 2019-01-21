from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import EventSerializers
from .models import Event

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the event index.")


@csrf_exempt
def event_detail(request, pk):
    """
    Get detail event by id 
    """
    try:
        event = Event.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = EventSerializers(event)
        return JsonResponse(serializer.data)
    else:
        return HttpResponse(status=404)
