
from flask import render_template
from . import home_bp
from app.models.models import TechStack
from collections import defaultdict


def type_priority(type_name):
    normalized = (type_name or '').strip().lower()
    if 'front' in normalized:
        return 0
    if 'back' in normalized:
        return 1
    if 'database' in normalized or 'base de datos' in normalized:
        return 2
    if 'devops' in normalized:
        return 3
    return 99


def build_techstack_by_type(use_spanish=False):
    techstack = TechStack.query.all()
    techstack.sort(
        key=lambda tech: (
            type_priority(tech.spanish_type if use_spanish else tech.type),
            ((tech.spanish_type if use_spanish else tech.type) or '').lower(),
            (tech.name or '').lower()
        )
    )

    techstack_by_type = defaultdict(list)
    for tech in techstack:
        group_type = tech.spanish_type if use_spanish else tech.type
        if use_spanish:
            techstack_by_type[group_type].append({
                'name': tech.name,
                'tech_type': tech.tech_type,
                'opinion': tech.spanish_opinion,
            })
        else:
            techstack_by_type[group_type].append(tech)

    return dict(techstack_by_type)

@home_bp.route('/markus-tech-stack')
def markus_tech_stack():
    return render_template('markus_tech_stack.html', techstack_by_type=build_techstack_by_type())

@home_bp.route('/es/markus-tech-stack')
def markus_tech_stack_es():
    return render_template('es/markus_tech_stack.html', techstack_by_type=build_techstack_by_type(use_spanish=True))