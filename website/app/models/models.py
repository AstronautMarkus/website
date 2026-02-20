from .. import db

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    username = db.Column(db.String(20), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'content': self.content,
            'username': self.username
        }