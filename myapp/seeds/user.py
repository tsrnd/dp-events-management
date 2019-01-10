from django.contrib.auth import get_user_model


def create_superuser():
    User = get_user_model()
    try:
        User.objects.get(username='admin')
    except:
        User.objects.create_superuser('admin', 'admin@localhost', 'admin')
