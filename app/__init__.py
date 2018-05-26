from flask import Flask, render_template

def create_app(config):
    app = Flask(__name__)

    app.config.from_object(config)

    @app.errorhandler(404)
    def not_found(error):
        return render_template('404.html'), 404

    @app.route('/')
    def index():
        return render_template('index.html')

    return app