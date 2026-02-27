from flask import render_template
from . import home_bp
from app.models.models import PortfolioProject, ProjectTechTag

@home_bp.route('/portfolio')
def portfolio():
    projects = PortfolioProject.query.order_by(PortfolioProject.id.desc()).all()
    return render_template('/home/portfolio.html', projects=projects)

@home_bp.route('/es/portfolio')
def portfolio_es():
    projects = PortfolioProject.query.order_by(PortfolioProject.id.desc()).all()
    return render_template('/home/es/portfolio.html', projects=projects)