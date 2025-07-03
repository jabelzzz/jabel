from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Primero creamos la instancia de SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    from app import routes
    routes.init_app(app)
    
    return app