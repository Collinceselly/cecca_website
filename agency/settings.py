"""
Django settings for agency project.

Generated by 'django-admin startproject' using Django 5.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-wm37!0o#e9@u&3*+pxk$(2^(ewgn7d9ay$@dikou#+#m)ren_u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'e655-102-217-64-113.ngrok-free.app']


# Add CSRF_TRUSTED_ORIGINS
CSRF_TRUSTED_ORIGINS = [
    'https://e655-102-217-64-113.ngrok-free.app',
    'http://127.0.0.1:8080',  # Optional: Include localhost for local testing
    'http://localhost:8080',  # Optional: Include localhost for local testing
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myApplication',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'agency.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
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

# # Pesapal API Credentials
# PESAPAL_CONSUMER_KEY = "MjNCfblEL4FLzcXEVVj6CtwBEpE+WjR2"
# PESAPAL_CONSUMER_SECRET = "R9Kuxw6MSepuE2wxB7muS8BeR5o="

# # Pesapal Endpoints (Sandbox URLs for testing, switch to Live URLs when ready)
# PESAPAL_OAUTH_URL = "https://cybqa.pesapal.com/pesapalv3/api/Auth/RequestToken"  # Sandbox
# PESAPAL_ORDER_URL = "https://cybqa.pesapal.com/pesapalv3/api/Transactions/SubmitOrderRequest"  # Sandbox
# PESAPAL_CHECK_STATUS_URL = "https://cybqa.pesapal.com/pesapalv3/api/Transactions/GetTransactionStatus"  # Sandbox


# settings.py
PESAPAL_API_URL = 'https://cybqa.pesapal.com/pesapalv3'
PESAPAL_CONSUMER_KEY = "qkio1BGGYAXTu2JOfm7XSXNruoZsrqEW" # Replace with your Consumer Key
PESAPAL_CONSUMER_SECRET = "osGQ364R49cXKeOYSpaOnT++rHs="  # Replace with your Consumer Secret
PESAPAL_CALLBACK_URL = 'https://e655-102-217-64-113.ngrok-free.app/payment-callback'  # Replace with your callback URL
PESAPAL_IPN_URL = 'https://e655-102-217-64-113.ngrok-free.app/ipn-callback'  # Replace with your IPN URL


WSGI_APPLICATION = 'agency.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'omondicolli@gmail.com'
EMAIL_HOST_PASSWORD = 'gbgd cwxd uqev mnar'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
CONTACT_EMAIL = 'omondicolli@gmail.com'

# MESSAGE_TAGS = {
#     'success': 'sent-message',
#     'error': 'error-message',
# }



# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
