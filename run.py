import os
from flask.helpers import get_debug_flag
from app import create_app
from app.settings import ProductionConfig, DevelopmentConfig

CONFIG = DevelopmentConfig if get_debug_flag() else ProductionConfig

app = create_app(CONFIG)

app.run(host=os.getenv('APP_HOST', default='0.0.0.0'), 
        port=os.getenv('APP_PORT', default=5000))