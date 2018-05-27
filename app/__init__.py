from flask import Flask, Blueprint, render_template
from flask_restful import Api
from app.resources.documents import Compare

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    api_bp = Blueprint('api', __name__)
    api = Api(api_bp)
    api.add_resource(Compare, '/api/documents/compare')
    app.register_blueprint(api_bp)

    @app.errorhandler(404)
    def not_found(error):
        return render_template('404.html'), 404

    @app.route('/')
    def index():
        return render_template('index.html')

    return app