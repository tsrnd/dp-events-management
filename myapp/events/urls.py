from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('events', views.PublicEventList.as_view(), name = 'events')
]
