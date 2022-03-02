# brightidsocial

A backend service to help BrightID users find their friends

## Local Development
(It's better to use a virtual env)
```
# install the dependencies
pip install -r requirements.txt

# run migrations and setup database
python manage.py migrate

# run the project
python manage.py runserver
```
Also, read the load initial data section

## Production
Use guides like this one https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-centos-7 to setup this Django
project on your server. You can rename `secret-sample.py` to `secret.py` to add your production configurations

## Load Initial Data
after running migrations, you can load initial social media variations to database
```
# running python shell for Django
python manage.py shell

from initial_data.initial_social_media import *
    upsert_initial_social_media_variations()
```
