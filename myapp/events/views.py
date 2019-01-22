from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import EventSerializers
from .models import Event

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the event index.")


@csrf_exempt
def event_detail(request, id_event):
    """
    Get detail event by id
    """
    try:
        event = Event.objects.get(pk=id_event)
    except:
        return JsonResponse({
            "message": "Id does not exist",
            "errors": [
                "string"
            ]
        }, status=500)

    if request.method == 'GET':
        serializer = EventSerializers(event)
        return JsonResponse(serializer.data, status=200)
    else:
        return JsonResponse({
            "message": "Request Forbiden",
            "errors": [
                "string"
            ]
        }, status=403)
