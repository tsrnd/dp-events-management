from django.urls import path

from . import views

urlpatterns = [
    path('logout', views.UserView.as_view(), name='logout'),
]
