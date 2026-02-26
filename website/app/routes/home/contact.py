from flask import render_template, request, redirect, url_for
from sqlalchemy.exc import SQLAlchemyError
from app import db
from app.models.models import ContactMessage
from . import home_bp

@home_bp.route('/contact')
def contact():
    return render_template('contact.html')

@home_bp.route('/es/contact')
def contact_es():
    return render_template('/es/contact.html')


@home_bp.route('/contact/submit', methods=['POST'])
def submit_contact_message():
    name = request.form.get('name', '').strip()
    email = request.form.get('_replyto', '').strip()
    message = request.form.get('message', '').strip()
    locale = request.form.get('locale', 'en').strip().lower()

    if locale not in {'en', 'es'}:
        locale = 'en'

    redirect_endpoint = 'home.contact_es' if locale == 'es' else 'home.contact'

    if not name or not email or not message:
        return redirect(url_for(redirect_endpoint, status='error'))

    if len(name) > 100 or len(email) > 120 or len(message) > 1000:
        return redirect(url_for(redirect_endpoint, status='error'))

    try:
        contact_message = ContactMessage(name=name, email=email, message=message)
        db.session.add(contact_message)
        db.session.commit()
    except SQLAlchemyError:
        db.session.rollback()
        return redirect(url_for(redirect_endpoint, status='error'))

    return redirect(url_for(redirect_endpoint, status='success'))