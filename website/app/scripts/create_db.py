import os
import sys

project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

from app import create_app
from app.models.models import db

import json
from app.models.models import TechStack, PortfolioProject, TechTag, ProjectTechTag

def load_techstack_data():
    json_path = os.path.join(os.path.dirname(__file__), 'techstack_data.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_portfolio_data():
    json_path = os.path.join(os.path.dirname(__file__), 'portfolio_data.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def init_database():
    """Initialize the database by creating tables and inserting tech stack and portfolio data."""
    app = create_app()
    with app.app_context():
        print("Creating tables...")
        db.create_all()
        print("Tables created successfully")
        # Insert tech stack data
        techstack_data = load_techstack_data()
        for item in techstack_data:
            exists = TechStack.query.filter_by(name=item['name'], type=item['type']).first()
            if not exists:
                db.session.add(TechStack(**item))
        db.session.commit()
        print("Tech stack data inserted.")
        # Insert portfolio projects and tags
        portfolio_data = load_portfolio_data()
        tag_cache = {}
        for project in portfolio_data:
            # Insert tags if not exist
            tag_ids = []
            for tag_name in project['tags']:
                tag = TechTag.query.filter_by(name=tag_name).first()
                if not tag:
                    tag = TechTag(name=tag_name)
                    db.session.add(tag)
                    db.session.flush()  # Get tag.id
                tag_ids.append(tag.id)
            db.session.flush()
            p = PortfolioProject(
                title=project['title'],
                description=project['description'],
                project_url=project['project_url']
            )
            db.session.add(p)
            db.session.flush()
            for tag_id in tag_ids:
                db.session.add(ProjectTechTag(project_id=p.id, tech_tag_id=tag_id))
        db.session.commit()
        print("Portfolio projects and tags inserted.")

def reset_database():
    """Delete all tables and recreate them."""
    app = create_app()
    with app.app_context():
        print("Deleting tables...")
        db.drop_all()
        print("Tables deleted")
        init_database()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        flag = sys.argv[1]
        if flag == "--reset":
            reset_database()
        else:
            print(f"Invalid flag: {flag}")
            print("Valid flag: --reset")
            print("No action was performed.")
    else:
        init_database()