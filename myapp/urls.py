from django.urls import path, include

urlpatterns = [
    path('comment/', include('comments.urls')),
    path('notification/', include('notifications.urls')),
    path('event/', include('events.urls')),
    path('snippet/', include('myapp.snippets.urls')),
]
