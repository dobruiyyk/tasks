def django_settings_context(request):
    import settings
    return settings.__dict__