from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status, mixins, generics

from django.http import Http404
from django.db import connection
import sys
from .models import Snippet, Post
from .serializers import SnippetSerializer, CustomeSerializer, JoinColumnSerializer, PostSerializer


class SnippetList(mixins.ListModelMixin, mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        sys.stdout.write('SnippetList get\n')
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        sys.stdout.write('SnippetList post\n')
        return self.create(request, *args, **kwargs)


class SnippetDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        """ Default statement for get Snippet detail.
        sys.stdout.write('SnippetDetail get\n')
        return self.retrieve(request, *args, **kwargs)
        """
        """ Custom SQL statement. """
        sys.stdout.write('Request :\n' + str(request))
        sys.stdout.write('args :\n' + str(args))
        sys.stdout.write('kwargs :\n' + str(kwargs))
        """with connection.cursor() as cursor:
            cursor.execute("SELECT title, language FROM tbl_snipplet WHERE id = %s", request.GET.get('pk',''))
            row = cursor.fetchone()

        return row"""
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        sys.stdout.write('SnippetDetail put\n')
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        sys.stdout.write('SnippetDetail delete\n')
        return self.destroy(request, *args, **kwargs)


class SnipListView(ListAPIView):
    queryset = Snippet.objects.raw(
        "SELECT id, title FROM tbl_snipplet GROUP BY id, title order by count(*) desc LIMIT 10"
    )
    serializer_class = CustomeSerializer

    def list(self, request):
        queryset = self.get_queryset()
        sys.stdout.write('Queryset : ' + str(queryset))
        # the serializer didn't take my RawQuerySet, so made it into a list
        serializer = CustomeSerializer(list(queryset), many=True)
        return Response(serializer.data)


class JoinListView(ListAPIView):
    queryset = Snippet.objects.raw(
        "SELECT tbl_snipplet.id as id, tbl_snipplet.title as title, tbl_post.content as content FROM tbl_snipplet JOIN tbl_post ON tbl_post.snipid = tbl_snipplet.id GROUP BY tbl_snipplet.id, tbl_snipplet.title, content order by tbl_snipplet.id LIMIT 10"
    )
    serializer_class = JoinColumnSerializer

    def list(self, request):
        queryset = self.get_queryset()
        sys.stdout.write('Queryset : ' + str(queryset))
        # the serializer didn't take my RawQuerySet, so made it into a list
        serializer = JoinColumnSerializer(list(queryset), many=True)
        return Response(serializer.data)


class ListPost(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class FilterPostBySnippet(ListAPIView):
    serializer_class = PostSerializer

    """ Set Filter by column. """
    def get_queryset(self):
        return Post.objects.filter(snipid=self.kwargs.get('pk', ''))
