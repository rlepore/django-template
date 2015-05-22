# django-template

Template to provide defaults for new Django 1.8+ projects based on best practices and some of my personal preferences.

## Usage

To create a new django project with this template:

```
django-admin.py startproject --template=https://github.com/rlepore/django-template/archive/latest.zip --extension=py,gitignore project_name
```

Install requirements via pip:

```
pip install -r requirements.txt
```

Run database migrations:

```
python manage.py migrate
```

## HTTPS
There is really no excuse to be running your site over http anymore.  The production settings file has been configured to take advantage of a small set of security wins provided by django.  Inorder to check your site settings run the following (this is now installed by default as of 1.8):

```
python manage.py check --deploy
```

https://docs.djangoproject.com/en/1.8/topics/security/
https://docs.djangoproject.com/en/1.8/releases/1.8/#security-enhancements
https://docs.djangoproject.com/en/1.8/ref/middleware/#django.middleware.security.SecurityMiddleware

## Links

- Layout is heavily influenced by: https://github.com/lincolnloop/django-layout