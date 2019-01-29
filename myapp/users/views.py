from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status


class UserView(APIView):
    def post(self, request):
        user = Token.objects.get(user_id=request.user.id).delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
