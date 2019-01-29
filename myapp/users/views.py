from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserView(APIView):
    def delete(self, request):
        token = request.META.get('HTTP_AUTHORIZATION').split(" ")
        if len(token) != 2:
            Response({"detail": "Invalid token."}, status=401)
        print(token[1])
        try:
            user = Token.objects.get(key=token[1]).delete()
        except Token.DoesNotExist:
            return Response({"detail": "Invalid token."}, status=401)

        return Response()
