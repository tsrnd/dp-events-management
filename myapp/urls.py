from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('comment/', include('myapp.comments.urls')),
    path('notification/', include('myapp.notifications.urls')),
    path('event/', include('myapp.events.urls')),
    path('snippet/', include('myapp.snippets.urls')),
    path('login', obtain_auth_token, name='login')
]
