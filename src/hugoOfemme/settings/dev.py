from .base import *
import os

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), "static"),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hugoofemme',
        'USER': 'juancarrizo',
        'PASSWORD': 'Carry_43346436',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}

DEBUG = True