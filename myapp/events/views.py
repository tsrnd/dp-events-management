from rest_framework.parsers import FormParser
from django.http import JsonResponse
from myapp.events.serializers import EventSerializer
from rest_framework.decorators import api_view
from rest_framework import status

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
