from api_config import db


class Cliente(db.Model):
    __tablename__ = "cliente"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(500), nullable=False)
    email  = db.Column(db.String(150), nullable=True)

