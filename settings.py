"""
Django settings for rthitha project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf import global_settings

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

import rthithasite

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'rfj)_%md*4!g)l77*!-w-qs-*fq&ik5)n(@3&axdbne2dj%q@m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['www.rthitha.com']

#ADMIN_MEDIA_PREFIX = '/static/admin/'
AUTH_PROFILE_MODULE = 'zmovies.UserProfile'
# Application definition

INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',

	'south',
	'zmovies',
	'tvseries',
	'social_auth',

    'rthitha_comments',
    'django.contrib.comments',
    'django.contrib.sites',
    'mptt',

)

COMMENTS_APP = 'rthitha_comments'
SITE_ID = 1

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'rthithasite.urls'

#WSGI_APPLICATION = 'rthitha.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'cizrage$rthitha',
		'USER': 'cizrage',
		'PASSWORD': 'ygmfromthuya',
		'HOST': 'mysql.server',
		'PORT': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    # PROJECT_PATH + '/templates/',
    os.path.join(PROJECT_PATH,'rthithasite/' 'templates')
)

MEDIA_ROOT = os.path.join(PROJECT_PATH,'rthithasite/' 'media')


AUTHENTICATION_BACKENDS = (
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.google.GoogleOAuthBackend',
    'social_auth.backends.google.GoogleOAuth2Backend',
    'social_auth.backends.google.GoogleBackend',
    'social_auth.backends.yahoo.YahooBackend',
    'social_auth.backends.browserid.BrowserIDBackend',
    'social_auth.backends.contrib.linkedin.LinkedinBackend',
    'social_auth.backends.contrib.disqus.DisqusBackend',
    'social_auth.backends.contrib.livejournal.LiveJournalBackend',
    'social_auth.backends.contrib.orkut.OrkutBackend',
    'social_auth.backends.contrib.foursquare.FoursquareBackend',
    'social_auth.backends.contrib.github.GithubBackend',
    'social_auth.backends.contrib.vk.VKOAuth2Backend',
    'social_auth.backends.contrib.live.LiveBackend',
    'social_auth.backends.contrib.skyrock.SkyrockBackend',
    'social_auth.backends.contrib.yahoo.YahooOAuthBackend',
    'social_auth.backends.contrib.readability.ReadabilityBackend',
    'social_auth.backends.contrib.fedora.FedoraBackend',
    'social_auth.backends.OpenIDBackend',
    'django.contrib.auth.backends.ModelBackend',
)

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',
    'social_auth.context_processors.social_auth_by_type_backends',
    'django.core.context_processors.request',
)

GOOGLE_OAUTH2_CLIENT_ID='310327175751-vafscehg8fatr0879lijimodg8cnc1m1.apps.googleusercontent.com'
GOOGLE_OAUTH2_CLIENT_SECRET='r1JCpHS_kf1cUghRt6SluNNf'

FACEBOOK_APP_ID='811252922227068'
FACEBOOK_API_SECRET='f061eef301363f074c0c8cd0cbea7121'

FACEBOOK_EXTENDED_PERMISSIONS = ['email']

#SOCIAL_AUTH_DEFAULT_USERNAME = 'new_social_auth_user'
#SOCIAL_AUTH_UID_LENGTH = 16
#SOCIAL_AUTH_ASSOCIATION_HANDLE_LENGTH = 16
#SOCIAL_AUTH_NONCE_SERVER_URL_LENGTH = 16
#SOCIAL_AUTH_ASSOCIATION_SERVER_URL_LENGTH = 16
#SOCIAL_AUTH_ASSOCIATION_HANDLE_LENGTH = 16


SOCIAL_AUTH_PIPELINE = (
    'social_auth.backends.pipeline.social.social_auth_user',
    #'social_auth.backends.pipeline.associate.associate_by_email',
    'social_auth.backends.pipeline.user.get_username',
    'social_auth.backends.pipeline.user.create_user',
    'social_auth.backends.pipeline.social.associate_user',
    'social_auth.backends.pipeline.social.load_extra_data',
    'social_auth.backends.pipeline.user.update_user_details',
    'rthithasite.pipeline.get_user_avatar',
)

SESSION_SERIALIZER='django.contrib.sessions.serializers.PickleSerializer'

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/private/'
LOGIN_ERROR_URL = '/login-error/'



try:
    from local_settings import *
except ImportError:
    print u'File local_settings.py is not found. Continuing with production settings.'