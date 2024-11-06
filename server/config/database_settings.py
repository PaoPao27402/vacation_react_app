import os


LOCAL_DATABASE = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('MYSQL_DATABASE', 'travel_agency'),
        'USER': os.environ.get('MYSQL_USER', 'root'),
        'PASSWORD': os.environ.get('MYSQL_PASSWORD', 'P@22word2710'),
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

DOCKER_DATABASE = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('MYSQL_DATABASE', 'travel_agency'),
        'USER': os.environ.get('MYSQL_USER', 'root'),
        'PASSWORD': os.environ.get('MYSQL_PASSWORD', 'P@22word2710'),
        'HOST': 'database-service',
        'PORT': '3306',
    }
}

if os.environ.get('DJANGO_ENVIRONMENT') == 'docker':
    DATABASES = DOCKER_DATABASE
else:
    DATABASES = LOCAL_DATABASE