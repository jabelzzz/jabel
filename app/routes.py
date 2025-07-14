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
        # Link skills with projects by name
        skill_lookup = {s['name']: s for s in skills}
        for project in projects:
            # Transform project skills from names to skill objects
            if 'skills' in project:
                project_skills = []
                for skill_name in project['skills']:
                    if skill_name in skill_lookup:
                        project_skills.append(skill_lookup[skill_name])
                project['skills'] = project_skills
        return render_template('index.html', skills=skills, projects=projects)
