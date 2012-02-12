all_tests : test 

test:
	@clear
	python manage.py test auth personal_info