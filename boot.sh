#!/bin/bash

while true; do
    python manage.py migrate
    if [[ "$?" == "0" ]]; then
        break
    fi
    echo Deploy command failed, retrying in 5 secs...
    sleep 5
done
exec gunicorn -c ./django/gunicorn.py qaschool.wsgi