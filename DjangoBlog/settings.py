import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = False
TESTING = len(sys.argv) > 1 and sys.argv[1] == 'test'

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'pagedown',
    'haystack',
    'blog',
    'accounts',
    'comments',
    'oauth',
    'servermanager',
    'compressor'
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'blog.middleware.OnlineMiddleware'
]

ROOT_URLCONF = 'DjangoBlog.urls'

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
                'blog.context_processors.seo_processor'
            ],
        },
    },
]

WSGI_APPLICATION = 'DjangoBlog.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DJANGO_DATABASE_NAME'),
        'USER': os.environ.get('DJANGO_DATABASE_USER'),
        'PASSWORD': os.environ.get('DJANGO_DATABASE_PASSWORD'),
        'HOST': os.environ.get('DJANGO_DATABASE_HOST'),
        'PORT': os.environ.get('DJANGO_DATABASE_PORT')
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

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


SITE_ROOT = os.path.dirname(os.path.abspath(__file__))
SITE_ROOT = os.path.abspath(os.path.join(SITE_ROOT, '../'))

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'DjangoBlog.whoosh_cn_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
    },
}
# 自动更新搜索索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
# 允许使用用户名或密码登录
AUTHENTICATION_BACKENDS = ['accounts.user_login_backend.EmailOrUsernameModelBackend']

STATIC_ROOT = os.path.join(SITE_ROOT, 'collectedstatic')

STATIC_URL = '/static/'
STATICFILES = os.path.join(BASE_DIR, 'static')

AUTH_USER_MODEL = 'accounts.BlogUser'
LOGIN_URL = '/login/'

TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
DATE_TIME_FORMAT = '%Y-%m-%d'

SITE_NAME = '湖风雨晚晴'
SITE_URL = 'http://www.zhiyuzhishan.com'
SITE_DESCRIPTION = '自强不息，止于至善'
SITE_SEO_DESCRIPTION = '小站主要用来分享和记录学习经验,教程,记录个人生活的点滴以及一些随笔.欢迎大家访问小站'
SITE_SEO_KEYWORDS = 'linux,database,数据库,服务器,ubuntu,shell,web,python,django,spark,人工智能,tensorflow'
ARTICLE_SUB_LENGTH = 300
SHOW_GOOGLE_ADSENSE = False
# bootstrap颜色样式
BOOTSTRAP_COLOR_TYPES = [
    'default', 'primary', 'success', 'info', 'warning', 'danger'
]

# 侧边栏文章数目
SIDEBAR_ARTICLE_COUNT = 10
# 侧边栏评论数目
SIDEBAR_COMMENT_COUNT = 5

# 分页
PAGINATE_BY = 5
# http缓存时间
CACHE_CONTROL_MAX_AGE = 2592000
# cache setting

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'TIMEOUT': 10800,
        'LOCATION': '127.0.0.1:11211',
    },
    'locmemcache': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'TIMEOUT': 10800,
        'LOCATION': 'unique-snowflake',
    }
}
CACHE_MIDDLEWARE_SECONDS = 60 * 60 * 10
CACHE_MIDDLEWARE_KEY_PREFIX = "djangoblog"
CACHE_MIDDLEWARE_ALIAS = 'default'

# SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# SESSION_CACHE_ALIAS = 'default'

OAHUTH = {
    'sina': {
        'appkey': os.environ.get('SINA_APP_KEY'),
        'appsecret': os.environ.get('SINA_APP_SECRET'),
        'callbackurl': 'http://www.lylinux.net/oauth/authorize?type=weibo'
    },
    'google': {
        'appkey': os.environ.get('GOOGLE_APP_KEY'),
        'appsecret': os.environ.get('GOOGLE_APP_SECRET'),
        'callbackurl': 'http://www.lylinux.net/oauth/authorize?type=google'
    },
    'github': {
        'appkey': os.environ.get('GITHUB_APP_KEY'),
        'appsecret': os.environ.get('GITHUB_APP_SECRET'),
        'callbackurl': 'http://www.lylinux.net/oauth/authorize?type=github'
    },
    'facebook': {
        'appkey': os.environ.get('FACEBOOK_APP_KEY'),
        'appsecret': os.environ.get('FACEBOOK_APP_SECRET'),
        'callbackurl': 'http://www.lylinux.net/oauth/authorize?type=facebook'
    }
}

SITE_ID = 1
BAIDU_NOTIFY_URL = "http://data.zz.baidu.com/urls?site=https://www.ly.net&token=1uAOGrMsUm5syDGn"

# Emial:
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_USE_TLS = True
# EMAIL_USE_SSL = True

EMAIL_HOST = 'smtp.zoho.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get('DJANGO_EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('DJANGO_EMAIL_PASSWORD')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = os.environ.get('DJANGO_EMAIL_USER')
# 设置debug=false 未处理异常邮件通知
ADMINS = [('xlhu', 'shaul.hu@gmail.com')]
# 微信管理员密码(两次md5获得)
WXADMIN = '995F03AC401D6CABABAEF756FC4D43C7'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s',
        },
        'simple': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'log_file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'djangoblog.log',
            'maxBytes': 16777216,  # 16 MB
            'formatter': 'verbose'
        },
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'null': {
            'class': 'logging.NullHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'djangoblog': {
            'handlers': ['log_file', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
    }
}

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other
    'compressor.finders.CompressorFinder',
)
COMPRESS_ENABLED = True
# COMPRESS_OFFLINE = True


COMPRESS_CSS_FILTERS = [
    # creates absolute urls from relative ones
    'compressor.filters.css_default.CssAbsoluteFilter',
    # css minimizer
    'compressor.filters.cssmin.CSSMinFilter'
]
COMPRESS_JS_FILTERS = [
    'compressor.filters.jsmin.JSMinFilter'
]
