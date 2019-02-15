from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('comments/', views.comments, name='comments'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('events/create', views.create_event, name='create-event'),
    path(
        'events/update/<int:id_event>',
        views.update_event,
        name='update-event'),
    path('events/<int:id_event>', views.detail_event, name='detail-event'),
]
