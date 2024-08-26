from flask import Flask
from src.app.controller.search_engine_controller import keyword_controller

def create_app():
    app = Flask(__name__)
    app.register_blueprint(keyword_controller, url_prefix='/api')

    @app.route('/')
    def index():
        return "Welcome to Merli Interface Search Engine!"

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
