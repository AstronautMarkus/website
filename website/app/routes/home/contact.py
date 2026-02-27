from datetime import datetime
from flask import render_template, request, redirect, url_for, flash, current_app
from flask_mail import Message
from sqlalchemy.exc import SQLAlchemyError
from app import db, mail
from app.models.models import ContactMessage
from . import home_bp

@home_bp.route('/contact')
def contact():
    return render_template('/home/contact.html')

@home_bp.route('/es/contact')
def contact_es():
    return render_template('/home/es/contact.html')


@home_bp.route('/contact/submit', methods=['POST'])
def submit_contact_message():
    name = request.form.get('name', '').strip()
    email = request.form.get('_replyto', '').strip()
    message = request.form.get('message', '').strip()
    locale = request.form.get('locale', 'en').strip().lower()

    if locale not in {'en', 'es'}:
        locale = 'en'

    redirect_endpoint = 'home.contact_es' if locale == 'es' else 'home.contact'
    success_message = '¡Gracias! Tu mensaje fue enviado correctamente.' if locale == 'es' else 'Thank you! Your message was sent successfully.'
    error_message = 'Hubo un problema al enviar tu mensaje. Revisa los datos e inténtalo de nuevo.' if locale == 'es' else 'There was a problem sending your message. Please check your information and try again.'

    if not name or not email or not message:
        flash(error_message, 'error')
        return redirect(url_for(redirect_endpoint))

    if len(name) > 100 or len(email) > 120 or len(message) > 1000:
        flash(error_message, 'error')
        return redirect(url_for(redirect_endpoint))

    try:
        contact_message = ContactMessage(name=name, email=email, message=message)
        db.session.add(contact_message)
        db.session.commit()
    except SQLAlchemyError:
        db.session.rollback()
        flash(error_message, 'error')
        return redirect(url_for(redirect_endpoint))

    try:
        send_contact_autoreply(email=email, name=name, locale=locale)
    except Exception:
        current_app.logger.exception('Failed to send contact auto-reply email')

    flash(success_message, 'success')
    return redirect(url_for(redirect_endpoint))


def send_contact_autoreply(email: str, name: str, locale: str = 'en') -> None:
    locale_code = 'es' if locale == 'es' else 'en'

    subject = 'Gracias por tu mensaje' if locale_code == 'es' else 'Thanks for your message'
    title = 'Mensaje recibido' if locale_code == 'es' else 'Message received'
    description = (
        f'Hola {name}, gracias por escribirme. Recibí tu mensaje y te responderé pronto.'
        if locale_code == 'es'
        else f'Hi {name}, thanks for reaching out. I received your message and will reply soon.'
    )

    html_body = render_template(
        'emails/email_response_template.html',
        title=title,
        description=description,
        year=datetime.now().year,
    )

    sender = (
        (current_app.config.get('MAIL_SENDER') or '').strip()
        or (current_app.config.get('MAIL_USERNAME') or '').strip()
    )
    if not sender:
        current_app.logger.warning('Auto-reply email skipped: MAIL_SENDER/MAIL_USERNAME is not configured')
        return

    message = Message(
        subject=subject,
        sender=sender,
        recipients=[email],
        html=html_body,
    )
    mail.send(message)