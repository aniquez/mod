# Django settings for MYPROJECT project.
import sys
import os

from path import path

SETTINGS_FILE_FOLDER = path(__file__).parent.abspath()
sys.path.append(SETTINGS_FILE_FOLDER.joinpath("../libs").abspath())

DEBUG = True
TEMPLATE_DEBUG = DEBUG
INTERNAL_IPS = ("127.0.0.1", "localhost")

COMPRESS_ENABLED=True

CACHE_MIDDLEWARE_SECONDS = 60*60  #60 minutes

CACHE_MIDDLEWARE_KEY_PREFIX = "myproject"

#for deployment, use memcache
if not DEBUG:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '127.0.0.1:11211',
        }
    }

SESSION_ENGINE = "django.contrib.sessions.backends.cache"

ADMINS = (
    ("Admin MyProject", "admin@email.com"),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'tmp',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': 'asd',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.

#TIME_ZONE = 'America/Chicago'
TIME_ZONE = 'Asia/Calcutta'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(SETTINGS_FILE_FOLDER,'../static')
COMPRESS_ROOT = MEDIA_ROOT
STATIC_PATH = '/static'
STATIC_URL = '/static/'

AUTH_USER_MODEL = 'core.User'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/static/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".

# Make this unique, and don't share it with anybody.
SECRET_KEY = '&l0*)nf6+^6r1(v+o5p3q1ax9g^xj9coc9xdjz&f_g*pgwhsdu'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'compressor.finders.CompressorFinder',
    )

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
   SETTINGS_FILE_FOLDER.joinpath("templates"),
)


TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'filebrowser',
    'grappelli', #must be before django.contrib.admin
    'django.contrib.admin',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.humanize',
    'django.contrib.markup',
    'compressor',

    'gunicorn',
    'south',
    #'django_extensions',
    'tagging',
    'tools',

    'core',
)


TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    #"django.core.context_processors.media",
    #"django.core.context_processors.static",
    #"django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
    "putils.context_processor",
)

#FILEBROWSER settings
FILEBROWSER_DIRECTORY = "uploads/articles/"

#django-tagging settings
FORCE_LOWERCASE_TAGS = True
MAX_TAG_LENGTH = 100

# python -m smtpd -n -c DebuggingServer localhost:1025
DEFAULT_FROM_EMAIL = "blubla@gmail.com"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_PASSWORD = '$%@WE234we__#'
EMAIL_HOST_USER = 'blubla@gmail.com'
EMAIL_PORT = '587'
EMAIL_USE_TLS = True

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

SITE_NAME = "MyProject"
SITE_URL = "http://myproject.com"
SITE_TITLE = "MyProject : Going good"
SITE_KEYWORDS = "myproject, django is cool, how to django, django my love, i love django"
SITE_DESCRIPTION = "A boilerplate for django projects, fitted with lots of regularly needed cool stuff"

#Put the following in local_settings when required
STATIC_PATH = "http://static.myproject.com/static"
COMPRESS_URL = "http://static.myproject.com/static/"
MEDIA_URL = "http://static.myproject.com/static/"

try:
    from local_settings import *
except ImportError:
    pass
