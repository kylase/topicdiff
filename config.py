DEBUG = True

import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

THREADS_PER_PAGE = 2

CSRF_ENABLED = True
CSRF_SESSION_KEY = os.getenv('APP_SECRET')
SECRET_KEY = os.getenv('APP_SECRET')