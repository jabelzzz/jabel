from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Creamos las instancias
db = SQLAlchemy()

def create_app():
    # Obtener la ruta absoluta al directorio de plantillas
    template_dir = os.path.abspath('templates')
    app = Flask(__name__, template_folder=template_dir)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Inicializamos la base de datos
    db.init_app(app)
    
    # Importamos los modelos
    from app import models
    
    # Creamos las tablas si no existen
    with app.app_context():
        db.create_all()
    
    # Configuramos las rutas
    from app import routes
    routes.init_app(app)
    
    return app