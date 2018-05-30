from flask import Flask, Blueprint, render_template
from flask_restful_swagger_2 import Api, get_swagger_blueprint
from flask_swagger_ui import get_swaggerui_blueprint
from app.resources.documents import Compare

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    API_DOC_PATH = '/api/docs'
    SWAGGER_PATH = '/api/swagger'

    api_bp = Blueprint('api', __name__)
    api = Api(api_bp, add_api_spec_resource=False)
    api.add_resource(Compare, '/api/documents/compare')

    docs = []
    docs.append(api.get_swagger_doc())

    swagger_ui_blueprint = get_swaggerui_blueprint(
        API_DOC_PATH,
        SWAGGER_PATH + '.json',
        config={
            'app_name': 'TopicDiff API'
        }
    )

    app.register_blueprint(api.blueprint)
    app.register_blueprint(get_swagger_blueprint(docs, SWAGGER_PATH, 
                                                 title='TopicDiff API', 
                                                 api_version='1.0',
                                                 base_path='/'))
    app.register_blueprint(swagger_ui_blueprint, url_prefix=API_DOC_PATH)

    @app.errorhandler(404)
    def not_found(error):
        return render_template('404.html'), 404

    @app.route('/')
    def index():
        return render_template('index.html')

    return app