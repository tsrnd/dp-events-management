from django.urls import path

from . import views

urlpatterns = [
    path('', views.EventList.as_view(), name='list_events'),
]
