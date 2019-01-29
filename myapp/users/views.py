from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import generics, permissions, status

from myapp.users import serializers
from myapp.users.serializers import UserRegistrationSerializer

class UserView(APIView):
    def post(self, request):
        user = Token.objects.get(user_id=request.user.id).delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class UserRegistrationAPIView(generics.CreateAPIView):
    """
        User registration.
    """
    permission_classes = (permissions.AllowAny, )
    serializer_class = serializers.UserRegistrationSerializer
