from flask import render_template
from app import db
from app.models import Skills, Projects

def init_app(app):
    @app.route('/')
    def index():
        skills = Skills.query.all()
        projects = Projects.query.all()
        return render_template('index.html', skills=skills, projects=projects)
    
    @app.route('/about')
    def about():
        return "Página Acerca de"