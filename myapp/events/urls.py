from django.urls import path

from . import views

urlpatterns = [
    path('<int:id_event>/users/', views.getUsers, name='getusers'),
]
