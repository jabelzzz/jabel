import yaml
from flask import render_template
import os

def load_yaml(filename):
    with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', filename), encoding='utf-8') as f:
        return yaml.safe_load(f)

def init_app(app):
    @app.route('/')
    def index():
        skills = load_yaml('skills.yaml')
        projects = load_yaml('projects.yaml')
        # Enlazar habilidades con los proyectos por nombre
        skill_lookup = {s['name']: s for s in skills}
        for project in projects:
            # Si existe la habilidad, adjunta el objeto completo
            if 'skill' in project and project['skill'] in skill_lookup:
                project['skill'] = skill_lookup[project['skill']]
        return render_template('index.html', skills=skills, projects=projects)

    @app.route('/about')
    def about():
        return "Página Acerca de"
