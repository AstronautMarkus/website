from flask import request, jsonify, redirect, url_for, flash
from . import home_bp
from app.models.models import Note, db

@home_bp.route('/note', methods=['POST'])
def post_note():

    import random
    if request.is_json:
        data = request.get_json()
        content = data.get('content') if data else None
        username = data.get('username') if data else None
        anonymous = data.get('anonymous', False)
    else:
        content = request.form.get('content')
        username = request.form.get('username')
        anonymous = request.form.get('anonymous') == 'on'


    errors = {}
    if not content or not isinstance(content, str) or not content.strip():
        errors['content'] = 'Content is required and must be a non-empty string.'

    # If anonymous is true, generate a random username regardless of the provided one
    if anonymous or not username or not isinstance(username, str) or not username.strip():
        username = f"Anonymous #{random.randint(1000, 9999)}"
    # If not anonymous but username is invalid, add an error
    elif not username or not isinstance(username, str) or not username.strip():
        errors['username'] = 'Username is required and must be a non-empty string.'

    if errors:
        if request.is_json:
            return jsonify({'errors': errors}), 400
        else:
            for field, msg in errors.items():
                if field in ('username', 'content'):
                    flash(msg, f'error_{field}')
                else:
                    flash(msg, 'error')
            return redirect(url_for('home.index'))

    new_note = Note(content=content.strip(), username=username.strip())
    try:
        db.session.add(new_note)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        if request.is_json:
            return jsonify({'error': 'Error saving the note.', 'details': str(e)}), 500
        else:
            flash(f'Error saving the note: {str(e)}', 'error')
            return redirect(url_for('home.index'))

    if request.is_json:
        return jsonify({'message': 'Note created successfully.', 'note': new_note.to_dict()}), 201
    else:
        flash('Note created successfully.', 'success')
        return redirect(url_for('home.index'))
