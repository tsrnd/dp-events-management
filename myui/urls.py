from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('comments/', views.comments, name='comments'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
]
