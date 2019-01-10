from django.urls import path, include

urlpatterns = [
    path('snippet/', include('myapp.snippets.urls')),
]
