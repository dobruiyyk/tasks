from django.conf import settings

def django_settings_context(request):
    return settings.__dict__