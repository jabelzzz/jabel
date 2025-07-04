from flask import Flask
import os

def create_app():
    template_dir = os.path.abspath('templates')
    app = Flask(__name__, template_folder=template_dir)
    # Registrar rutas
    from app import routes
    routes.init_app(app)
    return app
