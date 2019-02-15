from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import generics, permissions, status

from myapp.users import serializers
from myapp.users.serializers import UserRegistrationSerializer
from rest_framework.authtoken.views import ObtainAuthToken


class UserView(APIView):
    def post(self, request):
        user = Token.objects.get(user_id=request.user.id).delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class UserLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'id': token.user_id})


class UserRegistrationAPIView(generics.CreateAPIView):
    """
        User registration.
    """
    permission_classes = (permissions.AllowAny, )
    serializer_class = serializers.UserRegistrationSerializer
