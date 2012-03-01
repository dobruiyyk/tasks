MANAGE=django-admin.py

pyflakes:
	pyflakes apps settings.py urls.py

test:
	clear
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=settings $(MANAGE) test personal_info.AuthTestCase personal_info.FilesTestCase personal_info.FormTestCase tools.RequestMWTestCase tools.TemplateTagsTestCase tools.PrintModelsCommandTestCase

run:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=settings $(MANAGE) runserver

syncdb:
	touch temp.db
	rm temp.db
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=settings $(MANAGE) syncdb --noinput

windmill:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=settings $(MANAGE) test personal_info
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=settings $(MANAGE) test tools

shell:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=settings $(MANAGE) shell
