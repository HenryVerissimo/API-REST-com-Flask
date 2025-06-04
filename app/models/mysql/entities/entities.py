from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from sqlalchemy.orm import DeclarativeBase
from werkzeug.security import generate_password_hash, check_password_hash

class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
ma = Marshmallow()
migrate = Migrate()

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)

    def __init__(self, name:str, email:str, password:str) -> None:
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)

    def verify_password(self, password:str) -> bool:
        return check_password_hash(self.password, password)
    
    def __repr__(self) -> str:
        return f"<User(name:{self.name}, email:{self.email})>"
    

class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    id = ma.auto_field()
    name = ma.auto_field()
    email = ma.auto_field()

user_schema = UserSchema()
users_schema = UserSchema(many=True)
    