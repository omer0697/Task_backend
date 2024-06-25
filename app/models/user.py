from app import db

class Geo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lat = db.Column(db.String(100))
    lng = db.Column(db.String(100))
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=False)

    @property
    def serialize(self):
        return {
            'lat': self.lat,
            'lng': self.lng
        }
    

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(150))
    suite = db.Column(db.String(150))
    city = db.Column(db.String(150))
    zipcode = db.Column(db.String(50))
    geo = db.relationship('Geo', backref='address', uselist=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    @property
    def serialize(self):
        return {
            'street': self.street,
            'suite': self.suite,
            'city': self.city,
            'zipcode': self.zipcode,
            'geo': self.geo.serialize if self.geo else None
        }

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    catchPhrase = db.Column(db.String(250))
    bs = db.Column(db.String(150))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'catchPhrase': self.catchPhrase,
            'bs': self.bs
        }
    

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    phone = db.Column(db.String(50))
    website = db.Column(db.String(100))
    address = db.relationship('Address', backref='user', uselist=False)
    company = db.relationship('Company', backref='user', uselist=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    albums = db.relationship('Album', backref='author', lazy=True)
    todos = db.relationship('Todo', backref='author', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'
    
    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'username': self.username,
            'email': self.email,
            'phone': self.phone,
            'website': self.website,
            'address': self.address.serialize if self.address else None,
            'company': self.company.serialize if self.company else None,
            "geo": self.address.geo.serialize if self.address and self.address.geo else None,
        }
