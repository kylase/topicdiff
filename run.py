import os
from flask.helpers import get_debug_flag
from raven.contrib.flask import Sentry
from app import create_app
from app.settings import ProductionConfig, DevelopmentConfig

CONFIG = DevelopmentConfig if get_debug_flag() else ProductionConfig

app = create_app(CONFIG)

sentry = Sentry(app)

if __name__ == '__main__':
    app.run(host=os.getenv('HOST', default='0.0.0.0'),
            port=int(os.getenv('PORT', default='5000')))
