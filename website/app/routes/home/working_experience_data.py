from flask import render_template
from . import home_bp

from app.models.models import WorkExperience

@home_bp.route('/working-experience-data')
def working_experience_data():
    projects = WorkExperience.query.order_by(WorkExperience.id.desc()).all()
    return render_template('/home/working_experience_data.html', projects=projects)

@home_bp.route('/es/working-experience-data')
def working_experience_data_es():
    projects = WorkExperience.query.order_by(WorkExperience.id.desc()).all()
    return render_template('/home/es/working_experience_data.html', projects=projects)