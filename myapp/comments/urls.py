from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
     path('', views.CommentView.as_view(), name='comment_index'),
]
