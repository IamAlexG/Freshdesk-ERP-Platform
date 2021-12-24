"""
Title: Freshdesk CRM Platform.
Description: Freshdesk is smart ERP solution to manage your business. you can keep track of your inventory customers, products, orders, invoices, and more.
Author: Hossain Chisty(Backend Developer)
Contact: hossain.chisty11@gmail.com
Github: https://github.com/hossainchisty

"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-mqcg&7z#rec4yygir4_@&5ms0bno*9gribx$3@xwu#&-rvw$cs'

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']


DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
]

THIRD_PARTY_APPS = [
    'corsheaders',
    'import_export',
    'notifications',
    'user_sessions',
    'django_user_agents',
    'django.contrib.sitemaps',
    'django.contrib.humanize',
    'django_filters',
    'crispy_forms',
    'simple_history',
    'django_countries',
    'rest_framework',
    'phonenumber_field',
    'rest_framework.authtoken',
    'rest_auth',
    'rest_auth.registration',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django_otp',
    'django_otp.plugins.otp_totp',
    'django_otp.plugins.otp_static',
]

LOCAL_APPS = [
    'core.apps.CoreConfig',
    'stock.apps.StockConfig',
    'expense.apps.ExpenseConfig',
    'sales.apps.SalesConfig',
    'report.apps.ReportConfig',
    'service.apps.ServiceConfig',
    'returns.apps.ReturnsConfig',
    'damage.apps.DamageConfig',
    'settings.apps.SettingsConfig',
    'profiles.apps.ProfilesConfig',
    'products.apps.ProductsConfig',
    'accounts.apps.AccountsConfig',
    'purchase.apps.PurchaseConfig',
    'suppliers.apps.SuppliersConfig',
    'customers.apps.CustomersConfig',
]

INSTALLED_APPS = DEFAULT_APPS + LOCAL_APPS + THIRD_PARTY_APPS


SITE_ID = 1

ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': [    
#         # 'rest_framework.permissions.IsAuthenticated',
#         'rest_framework.permissions.AllowAny',
#     ],
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#     'rest_framework.authentication.TokenAuthentication',
#     'rest_framework.authentication.SessionAuthentication',
#     ],
#     'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
# }

REST_FRAMEWORK = {
    # 'SEARCH_PARAM': 'search'
    'SEARCH_PARAM': 'q'
}

# Setting the throttling policy

REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    # 'DEFAULT_THROTTLE_RATES': {
    #     'anon': '2/day',
    #     'user': '5/hour',
    #     'sale': '3/min',
    # }
}

# tailwind css pack
CRISPY_TEMPLATE_PACK = "bootstrap4"


DEFAULT_MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'user_sessions.middleware.SessionMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_otp.middleware.OTPMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

THIRD_PARTY_MIDDLEWARE = [
    'django_user_agents.middleware.UserAgentMiddleware',
]

MIDDLEWARE = DEFAULT_MIDDLEWARE + THIRD_PARTY_MIDDLEWARE

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # custom context processors📌
                'expense.context_processors.get_total_expsense',
                'expense.context_processors.get_total_expsense_by_month',
                'expense.context_processors.get_total_expsense_by_year',
            ],
        },
    },
]

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

# Mail configrations
# EMAIL_HOST = "smtp.zoho.com"
# EMAIL_PORT = 465
# EMAIL_HOST_USER = "hossain.chisty@zohomail.com"
# EMAIL_HOST_PASSWORD = "#2#3B399TiU@aBC"
# EMAIL_USE_SSL = True
# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

# Session configuration
# CART_SESSION_ID = 'cart'
SESSION_COOKIE_AGE = 86400  # 24 hours in seconds
SESSION_EXPIRE_AT_BROWSER_CLOSE = False

# Celery Configurations
CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
# CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Dhaka'

SESSION_ENGINE = 'user_sessions.backends.db'
# FIXME: Make sure LOGOUT_REDIRECT_URL is set to some page to redirect users after logging out.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'freshdesh-db.sqlite3',
    }
}

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.redis.RedisCache',
#         'LOCATION': 'redis://127.0.0.1:6379',
#     }
# }

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Dhaka'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']
DATA_UPLOAD_MAX_NUMBER_FIELDS = 10240

# A list of origins that are authorized to make cross-site HTTP requests.
# CORS_ALLOWED_ORIGINS = [
#     'http://127.0.0.1:9000',
# ]
CORS_ALLOW_ALL_ORIGINS = True

# Security Principles
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True
# SECURE_BROWSER_XSS_FILTER = True
# SECURE_HSTS_SECONDS = 31536000
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True
# SECURE_CONTENT_TYPE_NOSNIFF = True
# CSRF_COOKIE_SECURE = True
