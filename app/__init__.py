from flask import Flask
import os

def create_app():
    app = Flask(__name__, template_folder=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates'))
    # Registrar rutas
    from app import routes
    routes.init_app(app)
    return app
