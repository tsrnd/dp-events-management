from django.urls import path
from myapp.events import views

urlpatterns = [
    path('', views.EventList.as_view(), name='list_events'),
    path('<int:id_event>/', views.event_detail, name='detail'),
    path('<int:id_event>/users/', views.getUsers, name='getusers'),
]
