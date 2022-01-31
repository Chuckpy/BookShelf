import os
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env = environ.Env()
env.read_env(".env")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-inb secure-&07k4h=k&7bmq$1ersq1kytqxkg6h8no3e2v-eab#+vyfoh$ok'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.contenttypes',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_base64field',
    'django_extensions',
    'django_filters',
    'django_celery_results',
    'django_celery_beat',
    'social_django',
    # Meus apps
    'core.core_auth',
    'core.core_config',
    'conversare',
    'products',
    'project_auth',
    'ranking',
    # Apps terceiros
    'channels',
    'rangefilter',
    'oauth2_provider',
    'debug_toolbar',
    'rest_framework',
    'rest_framework.authtoken',  
    'rest_framework_social_oauth2',  
]


MIDDLEWARE = [
    #debug toolbar middleware
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR + '/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

TEMPLATE_CONTEXT_PROCESSORS = (
    'social_django.context_processors.backends',
    'social_django.context_processors.login_redirect',
)

WSGI_APPLICATION = 'project.wsgi.application'

ASGI_APPLICATION = 'project.routing.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('book_shelf_cache', 6379)],
        },
    },
}

# Chat config

MESSAGES_TO_LOAD = 15

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

db_user = env("POSTGRES_USER")
db_password = env("POSTGRES_PASSWORD")
db_port = int(env("DB_PORT"))

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": db_user,
        "USER": db_password,
        "PASSWORD": "postgres",
        "HOST": "db",
        "PORT": db_port,
    }
}

INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_USER_MODEL = "core_auth.CoreUser"

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Bahia'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = BASE_DIR+'/static/'

STATICFILES_DIRS = [f"{BASE_DIR}/static"]
STATIC_ROOT = f"{BASE_DIR}/staticfiles"


# Media

MEDIA_URL = f"{BASE_DIR}/media/"

MEDIA_ROOT = MEDIA_URL 


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Rest Framework

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES' :[
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework_social_oauth2.authentication.SocialAuthentication',
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 6,
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

AUTHENTICATION_BACKENDS = (
   'rest_framework_social_oauth2.backends.DjangoOAuth2',
   'django.contrib.auth.backends.ModelBackend',
)


#### Celery Configuration Options

CELERY_BROKER_URL = 'redis://book_shelf_cache:6379'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'


#### Django Celery Result options

CELERY_RESULT_BACKEND = 'django-db'
CELERY_CACHE_BACKEND = 'default'
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'my_cache_table',
    }
}




# Jazzmin admin template Configs : 

JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title":  "BookShelf",
    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Painel BookShelf",
    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "BookShelf",

    # Welcome text on the login screen
    "welcome_sign": "Bem vindo a prateleira de livros",
    # Copyright on the footer
    "copyright": "Solvum Ltd",
    # The model admin to search from the search bar, search bar omitted if excluded
    "search_model": "auth.User", 
    
    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "image/book.png",

    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Inicio",  "url": "admin:index", "permissions": ["auth.view_user"]},

        # external url that opens in a new window (Permissions can be added)
        {"name": "Suporte", "url": "https://github.com/Chuckpy/BookShelf/issues", "new_window": True},
        {"name": "Código Fonte", "url": "https://github.com/Chuckpy/BookShelf", "new_window": True},

        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},

        # App with dropdown menu to all its models pages (Permissions checked against models)
        {"app": "products"},
    ],

    # User Menu #

    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    "usermenu_links": [
        {"name": "Suporte", "url": "https://github.com/Chuckpy/BookShelf/issues", "new_window": True},
    ],


    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": ['products.ProductImages'],


    # Custom icons for side menu apps/models See
    # https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # for the full list of 5.13.0 free icon classes
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "products.Category": "fas fa-list",
        "products.SubCategory": "fas fa-archive",
        "products.Products": "fas fa-box-open",
        "products.Tag": "fas fa-tag",   
        "products.Like" :"fas fa-thumbs-up",
        "products.Dislike" :"fas fa-thumbs-down",
        "products.OpenSearch" :"fas fa-search-plus",     
        "project_auth.Client" :"fas fa-user-circle",
        "ranking.Rank" :"fas fa-chess-queen",
        "conversare.MessageModel":"far fa-comment",
        "core_config.ConfigApp" : "fas fa-cogs",
        "core_auth.CoreUser": "fas fa-address-card",
        "django_celery_results.TaskResult":"fas fa-poll",
        "django_celery_results.GroupResult":"fas fa-layer-group",
        "django_celery_beat.PeriodicTask": "fas fa-tasks",
        "django_celery_beat.IntervalSchedule": "fas fa-stopwatch",
        "django_celery_beat.CrontabSchedule": "fas fa-calendar-alt",
        "django_celery_beat.SolarSchedule": "fas fa-globe-americas",
        "django_celery_beat.ClockedSchedule": "fas fa-clock",
        "core_auth.CoreUser": "fas fa-address-card",        
    },
    
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "default",
    "dark_mode_theme": "darkly",
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-outline-info",
        "warning": "btn-outline-warning",
        "danger": "btn-outline-danger",
        "success": "btn-outline-success"
    }
}