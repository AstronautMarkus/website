from .. import db

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    username = db.Column(db.String(20), nullable=False)
    color = db.Column(db.Enum('red', 'blue', 'green', 'yellow', 'purple', 'orange', 'pink', 'gray'), nullable=False, default='gray')
    ip_address = db.Column(db.String(45), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

class TechStack(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    tech_type = db.Column(db.String(50), nullable=False)
    opinion = db.Column(db.String(500), nullable=False)

class PortfolioProject (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    project_url = db.Column(db.String(200), nullable=True)
    tech_tags = db.relationship('TechTag', secondary='project_tech_tag', backref='projects')

class TechTag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

class ProjectTechTag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('portfolio_project.id'), nullable=False)
    tech_tag_id = db.Column(db.Integer, db.ForeignKey('tech_tag.id'), nullable=False)