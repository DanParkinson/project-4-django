## Install Django and packages

- Install django with *pip3 install django~=4.2.1*
- Install gunicorn with *pip3 install gunicorn ~=20.1*
- Install whitenoise with *pip3 install whitenoise~=6.5.0*
- Install psycopg2 and dj_database_url with *pip3 install dj_database_url~=0.5 psycopg2~=2.9*

- Use command *pip3 freeze --local > requirements.txt* to create requirements.txt and add relavent packages to it.

![requirements.txt after install](docs/local_deployment/01-requirements.png)

## Create Django Project 

- Using the command *django-admin startproject elite .* creates our django project.

![Django Project Directory](docs/local_deployment/02-django-project.png)

## running the server and allowing hosts

Using the command *python3 manage.py runserver* opens the server in port 8000. The server needs allowed hosts in elite-cuisine/settings.py to be added.

![Disallowed host](docs/local_deployment/03-disallowed-host.png)

![Successful project](docs/local_deployment/04-install-succesful.png)