
import os
from pathlib import Path
from decouple import config
from django.contrib.messages import constants as messages
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = SECRET_KEY = config('SECRET_KEY')


DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'about.apps.AboutConfig',
    'category.apps.CategoryConfig',
    'comment.apps.CommentConfig',
    'product.apps.ProductConfig',
    'accounts.apps.AccountsConfig',
    'team.apps.TeamConfig',
    'tag.apps.TagConfig',
    'slider.apps.SliderConfig',
    'contact.apps.ContactConfig',
    'feedback.apps.FeedbackConfig',
    'django.contrib.sites',
    'newsletters.apps.NewslettersConfig',
    'ckeditor',
    'widget_tweaks',
    'users', 
    'allauth',
    'social_django',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google', # for Google OAuth 2.0
    'search.apps.SearchConfig',

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

ROOT_URLCONF = 'config.urls'

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
                'settings.context_processors.context_processors.products_view_context_processor',

            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'media', 'static'),
)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media', 'upload')

SITE_ID = 1
AUTH_USER_MODEL = 'accounts.User'

EMAIL_BACKEND = config('EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=True, cast=bool)


CACHES = {
   'default': {
      'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
      'LOCATION': 'my_cache_table',
   }
}



RECAPTCHA_PUBLIC_KEY = config("RECAPTCHA_PUBLIC_KEY",default="")
RECAPTCHA_PRIVATE_KEY = config("RECAPTCHA_PRIVATE_KEY",default="")


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.open_id.OpenIdAuth',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.google.GoogleOAuth',
)

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = config('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY') 
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = config('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')
SOCIAL_AUTH_URL_NAMESPACE = 'social'
ACCOUNT_EMAIL_VERIFICATION = None


LOGIN_REDIRECT_URL = "product:product_and_category"  
LOGOUT_REDIRECT_URL = 'login'


MESSAGE_TAGS = {
        messages.DEBUG: 'alert-secondary',
        messages.INFO: 'alert-info',
        messages.SUCCESS: 'alert-success',
        messages.WARNING: 'alert-warning',
        messages.ERROR: 'alert-error',
 }
MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"