from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 

class CommentView(APIView):
    permission_classes = (IsAuthenticated,) 
    def get(self, request):
        comment = {'comment': 'Hello, World!'}
        return Response(comment)