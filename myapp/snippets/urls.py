from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    # Get custome column from table through query.
    path('test', views.SnipListView.as_view(), name='listview'),
    # Join table Post and Snippet by Cusome query.
    path('join', views.JoinListView.as_view(), name='join'),
    # Join table Post and Snippet by Serializer.
    path('post', views.ListPost.as_view(), name='posts'),
    path('post/<int:pk>', views.FilterPostBySnippet.as_view(), name='findbysnipid'),
    # View detail by rule /api/snippet/2
    path('<int:pk>', views.SnippetDetail.as_view(), name='detail'),
    # View all snippets.
    path('', views.SnippetList.as_view(), name='index'),

    path('upload', views.FileView.as_view(), name='file-upload'),
    path('file/<int:pk>', views.FileDetail.as_view(), name='file-view'),
]

urlpatterns = format_suffix_patterns(urlpatterns)