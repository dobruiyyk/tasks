MANAGE=django-admin.py

test:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=settings $(MANAGE) test personal_info.LoginTestCase personal_info.FilesTestCase tools.RequestMWTestCase

run:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=settings $(MANAGE) runserver

syncdb:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=settings $(MANAGE) syncdb --noinput

windmill:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=settings $(MANAGE) test personal_info
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=settings $(MANAGE) test tools

shell:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=settings $(MANAGE) shell

pylint:
	pylint --generated-members=objects ../tasks