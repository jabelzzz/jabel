import sys
from pathlib import Path

# Añadir el directorio raíz al path de Python
root_dir = str(Path(__file__).parent.parent)
sys.path.append(root_dir)

from app import create_app, db
from app.models import Skills, Projects

def populate_database():
    app = create_app()
    
    with app.app_context():
        # Crear tablas si no existen
        db.create_all()
        
        print("🔨 Añadiendo datos de ejemplo...")
        
        # Crear habilidades si no existen
        skills_data = [
            {"name": "Python", "image": "python.svg"},
            {"name": "Flask", "image": "flask.svg"},
            {"name": "SQL", "image": "sqlite.svg"},
            {"name": "HTML5", "image": "html5.svg"},
            {"name": "CSS3", "image": "css.svg"},
            {"name": "JavaScript", "image": "javascript.svg"},
            {"name": "PostgreSQL", "image": "postgresql.svg"},
            {"name": "VMware", "image": "vmware.svg"}
        ]

        skills_added = 0
        skill_mapping = {}
        
        for data in skills_data:
            # Verificar si la habilidad ya existe
            skill = Skills.query.filter_by(name=data['name']).first()
            if not skill:
                skill = Skills(**data)
                db.session.add(skill)
                skills_added += 1
            skill_mapping[data['name']] = skill.id
        
        # Crear proyectos si no existen
        projects_data = [
            {
                "name": "Mi Portfolio",
                "description": "Portfolio personal desarrollado con Flask y Bootstrap",
                "image": "portfolio.png",
                "skill_id": skill_mapping.get("Python", 1)  # Usa el ID de Python
            },
            {
                "name": "Sistema de Gestión",
                "description": "Aplicación web para gestión de recursos",
                "image": "project2.png",
                "skill_id": skill_mapping.get("Flask", 2)  # Usa el ID de Flask
            }
        ]

        projects_added = 0
        for data in projects_data:
            if not Projects.query.filter_by(name=data['name']).first():
                project = Projects(**data)
                db.session.add(project)
                projects_added += 1
        
        # Guardar cambios
        db.session.commit()
        print("✅ Base de datos actualizada exitosamente!")
        print(f"   - {skills_added} nuevas habilidades añadidas")
        print(f"   - {projects_added} nuevos proyectos añadidos")

if __name__ == '__main__':
    populate_database()