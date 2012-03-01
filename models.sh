#!/bin/bash
#django command that prints all project models and the count of objects in every model

NOW=$(date +"%d.%b.%G")

FILE="$NOW.dat"
touch $FILE

echo `date +'%r'` >> $FILE
PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=settings python manage.py print_models 2>>$FILE