from api_config import db


class Pasaporte(db.Model):
    __tablename__ = "pasaporte"
    id = db.Column(db.Integer, primary_key=True)
    numero_pasaporte = db.Column(db.String(255), nullable=False)
    fecha_expiracion = db.Column(db.Date, nullable=False)
    cliente_id_fk = db.Column(db.Integer, db.ForeignKey("cliente.id"))
    cliente = db.relationship('Cliente', backref=db.backref('pasaporte', uselist=False))    #(uselist=False relacion uno a uno)establece la relacion entre la tabla cliente y el pasaporte. backref crea una referencia inversa para acceder a la relacion
    #id_cliente = db.relationship('Cliente', backref='pasaporte')    #devuelve una lista(relacion uno a varios)
    # fk_persona = db.Column(db.Integer, db.ForeignKey("persona.id"))
    # persona = db.relationship("Persona") 