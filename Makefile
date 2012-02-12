all_tests : test 

test:
	@clear
	python manage.py test personal_info
