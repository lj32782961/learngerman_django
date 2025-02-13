"""
Django settings for webapp project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-9i86l*nl5_t-ljr*7^1e4yqb!om@ds9_gxf)z$@=xcaar4%jqa'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["learngerman-ai.onrender.com","127.0.0.1"]#debug=True的时候，可以为空。为false的时候，开发环境下会返回错误。也可以添加“127.0.0.1”
CSRF_TRUSTED_ORIGINS = ["https://learngerman-ai.onrender.com/","https://learngerman-ai.onrender.com/chat"]#对于本项目来说，一定要加上https://learngerman-ai.onrender.com/chat/这个路径。因为fetch函数映射到该路径。否则返回的就不是token而是一个html


MY_API_KEY1 = os.environ.get('MY_API_KEY1')
MY_API_KEY2 = os.environ.get('MY_API_KEY2')
MY_API_KEY3 = os.environ.get('MY_API_KEY3')
MY_API_KEY4 = os.environ.get('MY_API_KEY4')
MY_API_KEY5 = os.environ.get('MY_API_KEY5')
MY_API_KEY6 = os.environ.get('MY_API_KEY6')
MY_API_KEY7 = os.environ.get('MY_API_KEY7')
MY_API_KEY8 = os.environ.get('MY_API_KEY8')
MY_API_KEY9 = os.environ.get('MY_API_KEY9')
MY_API_KEY10 = os.environ.get('MY_API_KEY10')
MY_API_KEY11 = os.environ.get('MY_API_KEY11')
MY_API_KEY12 = os.environ.get('MY_API_KEY12')
MY_API_KEY13 = os.environ.get('MY_API_KEY13')
MY_API_KEY14 = os.environ.get('MY_API_KEY14')

API_KEYS = [MY_API_KEY1,MY_API_KEY2,MY_API_KEY3,MY_API_KEY4,
            MY_API_KEY5,MY_API_KEY6,MY_API_KEY7,MY_API_KEY8,
            MY_API_KEY9,MY_API_KEY10,MY_API_KEY11,MY_API_KEY12,
            MY_API_KEY13,MY_API_KEY14]

API_KEYS = os.environ.get('MY_API_KEYS','').split(',')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'aichat',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

]

ROOT_URLCONF = 'webapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [], # 这里可以留空，Django 会自动查找各个 app 里的 templates 目录
        'APP_DIRS': True,# 确保启用 app 目录下的 templates 查找
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

WSGI_APPLICATION = 'webapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]#原来的是“STATICFILES_DIRS = os.path.join(BASE_DIR, 'static'),” 注意：双引号中的逗号不可以省略，不然报错。

# 生产环境下使用 `collectstatic` 统一收集静态文件的目标文件夹
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # 部署时使用
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'# 部署咋render.com时使用

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CACHES = {

    'default': {

        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',

    }

}

