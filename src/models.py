from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }



class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    age = Column(String(120), nullable=False)
    email = Column(String(120), nullable=False)
    favorites = relationship('Favorites', backref='user', lazy=True)


class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    population = Column(String(120), nullable=False)
    rotation = Column(String(120), nullable=False)  
    diameter = Column(String(120), nullable=False)   
    favorites = relationship('Favorites', backref='planets', lazy=True)


class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    gender = Column(String(120), nullable=False)
    height = Column(String(120), nullable=False)  
    eye_color = Column(String(120), nullable=False)   
    favoritos = relationship('Favoritos', backref='characters', lazy=True)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    model = Column(String(120), nullable=False)
    manufacturer = Column(String(120), nullable=False)  
    Cost_in_credits = Column(String(120), nullable=False)   
    favoritos = relationship('Favoritos', backref='vehicles', lazy=True)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'),
        nullable=False)
    planets_id = Column(Integer, ForeignKey('planets.id'),
        nullable=False)
    charancteres_id = Column(Integer, ForeignKey('characters.id'),
        nullable=False)
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'),
        nullable=False)

    def to_dict(self):
        return {}


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')