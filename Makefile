MANAGE=django-admin.py

test:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=settings $(MANAGE) test personal_info.FilesTestCase

run:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=settings $(MANAGE) runserver

syncdb:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=settings $(MANAGE) syncdb --noinput

windmill:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=settings $(MANAGE) test personal_info