"""
Django settings for labweb project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os 

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_URL = "/static/"

# 개발 중 정적 파일들을 찾을 추가적인 위치들
STATICFILES_DIRS = os.path.join(BASE_DIR, 'static'),
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# collectstatic 명령을 실행했을 때 정적 파일들이 저장될 경로
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# MEDIA
MEDIA_URL = '/upload/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'upload')

#STATICFILES_FINDERS = ['django.contrib.staticfiles.finders.FileSystemFinder',]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-@r)b+$dd#k^#_e+blqmke+ig3dp-sx%3h2&chr$ey(#!2(79x6"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
            # 도메인
            ".ines-lab.com",        
            ".www.ines-lab.com",
            ".ines-lab.gachon.ac.kr",
            # 퍼블릭 IPv4 DNS
            ".ap-northeast-2.compute.amazonaws.com",
            # 로드밸런서 & EC2 인스턴스 IP
            "54.180.207.234",  # 로드밸런서의 퍼블릭 IP 또는 DNS
            "172.31.13.26",     # EC2 인스턴스의 프라이빗 IP
            "15.164.35.55",     # 서버 IP 주소
            # 로컬
            "127.0.0.1"
]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "awards.apps.AwardsConfig",
    'django.contrib.humanize', #날짜 템플릿

    # 애플리케이션
    'ai.app.AiConfig',
    'hw.app.HwConfig',
    'member.apps.MemberConfig',
    'projects.apps.ProjectsConfig',
    'project.apps.ProjectConfig',
    'publications.apps.PublicationsConfig',
    'contact.apps.ContactConfig',
    'gallery.apps.GalleryConfig',
    'publication.apps.PublicationConfig',
    'area.apps.AreaConfig',
    'notice.apps.NoticeConfig',
    'history_of_ines.apps.HistoryOfInesConfig',

   
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "labweb.urls"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "labweb.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

CSRF_TRUSTED_ORIGINS = ['https://ines-lab.com']


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True



# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

