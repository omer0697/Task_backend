from app import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Boolean, default=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Todo {self.title}>'
    
    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'completed': self.completed,
            'user_id': self.user_id
        }
