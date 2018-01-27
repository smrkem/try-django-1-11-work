### Create a new django project using Docker

Create the project files:  
`docker-compose run --user 1000:1000 web django-admin.py startproject projectname .`

Set up the DB (in settings.py):  
```
DATABASES = {
  'default': {
      'ENGINE': 'django.db.backends.postgresql',
      'NAME': 'postgres',
      'USER': 'postgres',
      'HOST': 'db',
      'PORT': 5432,
  }
}
```

and then run with:  
`docker-compose up`


***  
- Install and setup pytest. Create test_settings.py.  
- Create settings module  

***
- `python manage.py migrate`  
- `python manage.py createsuperuser`
