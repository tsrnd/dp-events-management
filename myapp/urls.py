from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from myapp.users import views

urlpatterns = [
    path('comment/', include('myapp.comments.urls')),
    path('notification/', include('myapp.notifications.urls')),
    path('events/', include('myapp.events.urls')),
    path('users/', include('myapp.users.urls')),
    path('snippet/', include('myapp.snippets.urls')),
    path('login', views.UserLoginView.as_view(), name='login_index')
]
