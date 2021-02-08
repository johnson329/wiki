from .common import *
DEBUG = False
SECRET_KEY = '#8t=%obel7cq1hsh3kcoxffx+=i7arj68vjr5p#xi1x0#3#r!a'

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db2.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'mysql-container',
        'PORT': '3307',
        # 'NAME': '',
        'USER': 'wiki_user',
        'PASSWORD': 'wiki_user_123321',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            },
    }
}
