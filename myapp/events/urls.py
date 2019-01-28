from django.urls import path
from . import views

urlpatterns = [
    path('', views.EventView.as_view()),
    path('<int:id_event>/', views.event_detail, name='detail'),
    path('<int:id_event>/users/', views.getUsers, name='getusers'),
]
