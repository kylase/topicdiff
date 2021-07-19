import os
import sentry_sdk

from flask.helpers import get_debug_flag
from sentry_sdk.integrations.flask import FlaskIntegration

from app import create_app
from app.settings import ProductionConfig, DevelopmentConfig

CONFIG = DevelopmentConfig if get_debug_flag() else ProductionConfig

sentry_sdk.init(
    dsn=os.getenv('SENTRY_DSN'),
    integrations=[FlaskIntegration()],
    traces_sample_rate=1.0
)

app = create_app(CONFIG)

if __name__ == '__main__':
    app.run(host=os.getenv('HOST', default='0.0.0.0'),
            port=int(os.getenv('PORT', default='5000')))
