#!/bin/bash

echo '========== CHECKING FOR UNINSTALLED PKGs AND INSTALLING'
pip install -r requirements.txt

echo '========== MAKING MIGRATIONS'
python manage.py makemigrations

echo '========== RUNNING MIGRATIONS'
python manage.py migrate

echo '========== ENSURING ADMIN USER'
python manage.py ensure_adminuser --username=$SUPERUSER_USERNAME \
    --email=$SUPERUSER_EMAIL \
    --password=$SUPERUSER_PASSWORD

echo '========== RUNNING SERVER'
python manage.py runserver 0.0.0.0:8001

