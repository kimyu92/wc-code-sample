# SWE Fun Project
## Fifa World Cup'2014


## General development environment setup:
1. setup the environment below
2. install dependencies
3. setup db refer to [postgres-kimchi-reference](/src/db_data/postgresql-newbie-guide.md)
4. python manage.py runscripts generate-secret-key
6. setup the SECRET_KEY environment
7. run 3 data scripts eg. python manage.py runscripts insert-whatever-data
8. python3 manage.py runserver 8000

## Test model (Deprecated)
> preq: setup the model mentioned above 
> location: test_Model.py
> python3 manage.py test


## Setup fulltext search with django-watson
1. comment out app from settings.py
2. since django 1.8 AppConfig is required and configured to app.apps.WorldCupWatsonConfig in INSTALLED_APP and __init__.py in app folder
3. python manage.py buildwatson
4. index should have been updated


## Template debug on rendering html
* http://django-template-debug.readthedocs.org/en/latest/_templates/set_trace.html
* place this on html for debugging
```python
{% load debug_tags %} 
```
* eg. render to simulate the template rendering and available command such as details and variables
```python
render('{% if item.magical %}A magical item {% endif %}')
```
* caveat: iterable object have to be passed to html and eg of direct accessing list using VardotIndex


## Python Environment
### Mac
1. brew install pyenv
1. add below to .bash_profile
```bash
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```
3. brew install pyvenv
4. pyenv install 3.4.3 (or any version)
5. go to project directory and pyvenv my-env
6. source my-env/bin/activate
7. python or python3 --version should point to 3.4.3
8. pip install -U pip

### Ubuntu
1. sudo apt-get install virtualenv
1. virtualenv my-env -p /usr/bin/python3
1. source my-env/bin/activate
1. python --version
1. pip install -U pip

## Ultimate Deployment Gunicorn + Nginx

### Quick command for testing
1. gunicorn --bind 0.0.0.0:8000 myproject.wsgi:application

### Gunicorn setup
1. sudo vim /etc/init/gunicorn.conf
```shell
description "Gunicorn application server handling myproject"

start on runlevel [2345]
stop on runlevel [!2345]

respawn
setuid user
setgid www-data
chdir /home/user/myproject

exec myprojectenv/bin/gunicorn --workers 3 --bind unix:/home/user/myproject/myproject.sock myproject.wsgi:application
```
2. sudo service gunicorn start

### Nginx setup
1. sudo vim /etc/nginx/sites-available/myproject

```bash
server {
    listen 80;
    server_name server_domain_or_IP;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/user/myproject;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/user/myproject/myproject.sock;
    }
}
```

2. sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled
3. sudo nginx -t # Test Nginx configuration for syntax errors
4. sudo service nginx restart

## Slim down version of deployment Gunicorn Daemon and Nginx
* Setup everything and please do not use root user
```bash
* python manage.py collectstatic
```
```bash
* gunicorn worldcup.wsgi:application --bind=127.0.0.1:8001 --daemon
```
* nginx setup like below on eg /etc/nginx/sites-enabled/worldcup
```bash
server {
  listen 80; 
  server_name server_ip_or_address_domain;
  location / { 
    proxy_pass http://127.0.0.1:8001;
  }

  location /static/ {
    alias /home/whateverUser...../swe-worldcup/src/worldcup/staticfiles/;
  }
}
```

## Better? Deployment staticfiles with whitenoise in future
* https://warehouse.python.org/project/whitenoise/

## Dependencies
1. Python 3.4+
1. Django 1.8.7
1. Postgres 9.4
1. PyJade 3.1
1. Twitter Bootstrap
1. jQuery
1. Gunicorn
1. Nginx
1. and more ...


### Author:
* Kim Yu Ng
