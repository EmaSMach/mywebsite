import os
from .base import *

import dj_database_url

ALLOWED_HOSTS = ['*']
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

CSRF_TRUSTED_ORIGINS = [domain.strip() for domain in os.getenv('CSRF_TRUSTED_ORIGINS').split(',') if domain]
# CSRF_TRUSTED_ORIGINS = ['*']
