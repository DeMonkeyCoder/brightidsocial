import os
from pathlib import Path

SECRET_KEY = 'ttfq1pid2aa*#qxrbk($f%-7w6q5(=(ovt%c98!u0iqky52ngh'
ALLOWED_HOSTS = ['*']
DEBUG = True

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(os.path.join(BASE_DIR, "db.sqlite3"))
    }
}