from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from myapp.events.serializers import EventSerializer
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET', 'POST'])
def index(request):
    """
        Get Events
    """
    if request.method == 'GET':
        return HttpResponse("This is GET method")
    
    """
        Create a new Event
    """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EventSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
