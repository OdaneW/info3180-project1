from . import db

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique = True)
    no_of_bedrooms = db.Column(db.Integer)
    no_of_bathrooms = db.Column(db.Integer)
    location = db.Column(db.String(100), unique = True)
    price = db.Column(db.Integer)
    type = db.Column(db.String(20))
    description = db.Column(db.String(1000))
    photo = db.Column(db.String(50))

    def __init__(self,title, no_of_bedrooms, no_of_bathrooms, location, price, type, description, photo):
        self.title = title
        self.no_of_bedrooms = no_of_bedrooms
        self.no_of_bathrooms = no_of_bathrooms
        self.location = location
        self.price = price
        self.type = type
        self.description = description
        self.photo = photo

    def __repr__(self):
        return 'Property %r' % self.title
        
