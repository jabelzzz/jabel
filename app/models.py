from app import db

class Skills(db.Model):
    __tablename__ = 'skills'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    image = db.Column(db.String(200), default=None)    
    projects = db.relationship('Projects', backref='skill', lazy=True)

class Projects(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(200), default="")
    image = db.Column(db.String(200))
    skill_id = db.Column(db.Integer, db.ForeignKey('skills.id'), nullable=False)