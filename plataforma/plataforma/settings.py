"""
Django settings for plataforma project.

Generated by 'django-admin startproject' using Django 4.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from django.core.exceptions import ImproperlyConfigured
from django.urls import reverse_lazy



import os, json
from pathlib import Path
import sys
import environ

sys.modules['fontawesome_free'] = __import__('fontawesome-free')




# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

with open('secret.json') as f:
    secret= json.loads(f.read())

def get_secret(secret_name, secrets= secret):
    try:
        return secrets[secret_name]
    except:
        mgs= 'la variable %s no existe' % secret_name
        raise ImproperlyConfigured(mgs)
        

SECRET_KEY =  get_secret('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

MESSAGE_STORAGE= "django.contrib.messages.storage.cookie.CookieStorage"

# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap4',
    'django_bootstrap_icons',
    'import_export',
    'jquery',
    'javascript_settings',
    'fontawesomefree',
    'sweetify',
    
)

LOCAL_APPS = (
    'applications.Agenda',
    'applications.Finance',
    'applications.Homepage',
    'applications.Programs',
    'applications.Student',
    'applications.Teacher',
    'applications.User',
    'applications.Dashboard',


    
    
)


THIRD_PARTY_APPS = (
    
)

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

# possible options: 'sweetalert', 'sweetalert2' - default is 'sweetalert2'
SWEETIFY_SWEETALERT_LIBRARY = 'sweetalert2'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'plataforma.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'plataforma.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret('DB_NAME'),
        'USER': get_secret('USER'),
        'PASSWORD': get_secret('PASSWORD'),
        'HOST': 'localhost',
        'PORT': 5432,

        
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators


AUTH_USER_MODEL = 'User.User'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LOGIN_REDIRECT_URL = reverse_lazy('dashboard_app:dashboard-admin') # terminar el login
LOGOUT_REDIRECT_URL = reverse_lazy('homepage_app:login') 

#Variables de envio de emails
env = environ.Env()
environ.Env.read_env()
DEFAULT_FROM_EMAIL =get_secret("EMAIL_DEFAULT")
NOTIFY_EMAIL =get_secret("EMAIL_DEFAULT")
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = get_secret('EMAIL_HOST') 
EMAIL_HOST_USER =get_secret("EMAIL_DEFAULT")
EMAIL_HOST_PASSWORD = get_secret('EMAIL_PASSWORD')
RECIPIENT_ADDRESS = get_secret("EMAIL_DEFAULT")
EMAIL_PORT = 587 
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'es-co'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATIC_URL = '/static/'
MEDIA_URL= '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Configuraciones de seguridad

SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True

# Asegúrate de que el resto de tu configuración esté correctamente organizada y accesible