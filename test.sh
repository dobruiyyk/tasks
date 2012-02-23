rm temp.db
PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=settings django-admin.py syncdb --noinput