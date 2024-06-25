from app import db

class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    url = db.Column(db.String(300), nullable=False)
    thumbnail_url = db.Column(db.String(300), nullable=False)
    album_id = db.Column(db.Integer, db.ForeignKey('album.id'), nullable=False)

    def __repr__(self):
        return f'<Photo {self.title}>'
    
    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'url': self.url,
            'thumbnail_url': self.thumbnail_url,
            'album_id': self.album_id
        }
