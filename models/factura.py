from api_config import db


class Factura(db.Model):
    __tablename__ = "factura"
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False)
    monto = db.Column(db.Float, nullable=False)
    id_cliente_fk = db.Column(db.Integer, db.ForeignKey("cliente.id"))
    cliente = db.relationship('Cliente', backref='factura')    #establece la relacion entre la tabla cliente y el pasaporte. backref crea una referencia inversa para acceder a la relacion
    # fk_persona = db.Column(db.Integer, db.ForeignKey("persona.id"))
    # persona = db.relationship("Persona")