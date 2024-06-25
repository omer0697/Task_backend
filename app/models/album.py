from app import db

class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    photos = db.relationship('Photo', backref='album', lazy=True)

    def __repr__(self):
        return f'<Album {self.title}>'
    
    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'user_id': self.user_id,
            'photos': [photo.serialize for photo in self.photos]  # Nested serialization
        }
