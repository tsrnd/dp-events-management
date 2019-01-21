from django.urls import path, include

urlpatterns = [
    path('comment/', include('myapp.comments.urls')),
    path('notification/', include('myapp.notifications.urls')),
    path('events/', include('myapp.events.urls')),
    path('snippet/', include('myapp.snippets.urls')),
]
