from graphene import (
    ObjectType,
    Mutation,
    Int,
    String,
    Field,
    Date,
    Float,
    List
)
from api_config import (
    db,
)

from .objects import (
    Persona,
    Cliente,
    Pasaporte,
    Factura
)
from .persona import Persona as PersonaModel

#agregado por mi
from .cliente import Cliente as ClienteModel
from .pasaporte import Pasaporte as PasaporteModel
from .factura import Factura as FacturaModel


class createPersona(Mutation):
    class Arguments:
        name = String(required=True)
        last_name = String(required=True)
        email = String(required=False)
    
    persona = Field(lambda: Persona)

    def mutate(self, info, name, last_name, email=None):
        persona = PersonaModel(name=name, last_name=last_name, email=email)

        db.session.add(persona)
        db.session.commit()

        return createPersona(persona=persona)

class updatePersona(Mutation):
    class Arguments:
        persona_id = Int(required=True)
        email = String()
        name = String()
        last_name = String()

    persona = Field(lambda: Persona)

    def mutate(self, info, persona_id, email=None, name=None, last_name=None):
        persona = PersonaModel.query.get(persona_id)
        if persona:
            if email:
                persona.email = email
            if name:
                persona.name = name
            if last_name:
                persona.last_name = last_name
            db.session.add(persona)
            db.session.commit()

        return updatePersona(persona=persona)


class deletePersona(Mutation):
    class Arguments:
        persona_id = Int(required=True)

    persona = Field(lambda: Persona)

    def mutate(self, info, persona_id):
        persona = PersonaModel.query.get(persona_id)
        if persona:
            db.session.delete(persona)
            db.session.commit()

        return deletePersona(persona=persona)

#agregado por mi
#CLIENTE-----
class createCliente(Mutation):
    class Arguments:
        name = String(required=True)
        last_name = String(required=True)
        email = String(required=False)
    
    cliente = Field(lambda: Cliente)

    def mutate(self, info, name, last_name, email=None):
        cliente = ClienteModel(name=name, last_name=last_name, email=email)

        db.session.add(cliente)
        db.session.commit()

        return createCliente(cliente=cliente)

class updateCliente(Mutation):
    class Arguments:
        cliente_id = Int(required=True)
        email = String()
        name = String()
        last_name = String()

    cliente = Field(lambda: Cliente)

    def mutate(self, info, cliente_id, email=None, name=None, last_name=None):
        cliente = ClienteModel.query.get(cliente_id)
        if cliente:
            if email:
                cliente.email = email
            if name:
                cliente.name = name
            if last_name:
                cliente.last_name = last_name
            db.session.add(cliente)
            db.session.commit()

        return updateCliente(cliente=cliente)

class deleteCliente(Mutation):
    class Arguments:
        cliente_id = Int(required=True)

    cliente = Field(lambda: Cliente)

    def mutate(self, info, cliente_id):
        cliente = ClienteModel.query.get(cliente_id)
        if cliente:
            db.session.delete(cliente)
            db.session.commit()

        return deleteCliente(cliente=cliente)
# FIN CLIENTE-----

# PASAPORTE-----
class createPasaporte(Mutation):
    class Arguments:
        numero_pasaporte = String(required=True)
        fecha_expiracion = Date(required=True)
        cliente_id_fk = Int(required=True)
    
    pasaporte = Field(lambda: Pasaporte)

    def mutate(self, info, numero_pasaporte, fecha_expiracion, cliente_id_fk):
        pasaporte = PasaporteModel(numero_pasaporte=numero_pasaporte, fecha_expiracion=fecha_expiracion, cliente_id_fk=cliente_id_fk)

        db.session.add(pasaporte)
        db.session.commit()

        return createPasaporte(pasaporte=pasaporte)

class updatePasaporte(Mutation):
    class Arguments:
        idPasaporte = Int(required=True)
        numero_pasaporte = String()
        fecha_expiracion = Date()
        cliente_id_fk = Int()

    pasporte = Field(lambda: Pasaporte)

    def mutate(self, info, idPasaporte, numero_pasaporte=None, fecha_expiracion=None, cliente_id_fk=None):
        pasporte = PasaporteModel.query.get(idPasaporte)
        if pasporte:
            if numero_pasaporte:
                pasporte.numero_pasaporte = numero_pasaporte
            if fecha_expiracion:
                pasporte.fecha_expiracion = fecha_expiracion
            if cliente_id_fk:
                pasporte.cliente_id_fk = cliente_id_fk
            db.session.add(pasporte)
            db.session.commit()

        return updatePasaporte(pasporte=pasporte)

class deletePasaporte(Mutation):
    class Arguments:
        idPasaporte = Int(required=True)

    pasaporte = Field(lambda: Pasaporte)

    def mutate(self, info, idPasaporte):
        pasaporte = PasaporteModel.query.get(idPasaporte)
        if pasaporte:
            db.session.delete(pasaporte)
            db.session.commit()

        return deletePasaporte(pasaporte=pasaporte)
# FIN PASAPORTE-----

# FACTURA-----
class createFactura(Mutation):
    class Arguments:
        fecha = Date(required=True)
        monto = Float(required=True)
        id_cliente_fk = Int(required=True)
    
    factura = Field(lambda: Factura)

    def mutate(self, info, fecha, monto, id_cliente_fk):
        factura = FacturaModel(fecha=fecha, monto=monto, id_cliente_fk=id_cliente_fk)

        db.session.add(factura)
        db.session.commit()

        return createFactura(factura=factura)

class updateFactura(Mutation):
    class Arguments:
        idFactura = Int(required=True)
        fecha = Date()
        monto = Float()
        id_cliente_fk = Int()

    factura = Field(lambda: Factura)

    def mutate(self, info, idFactura, fecha=None, monto=None, id_cliente_fk=None):
        factura = FacturaModel.query.get(idFactura)
        if factura:
            if fecha:
                factura.fecha = fecha
            if monto:
                factura.monto = monto
            if id_cliente_fk:
                factura.id_cliente_fk = id_cliente_fk
            db.session.add(factura)
            db.session.commit()

        return updateFactura(factura=factura)

class deleteFactura(Mutation):
    class Arguments:
        idFactura = Int(required=True)

    factura = Field(lambda: Factura)

    def mutate(self, info, idFactura):
        factura = FacturaModel.query.get(idFactura)
        if factura:
            db.session.delete(factura)
            db.session.commit()

        return deleteFactura(factura=factura)

class deleteFacturaPorFecha(Mutation):
    class Arguments:
        fecha = Date(required=True)

    facturas = List(lambda: Factura)

    def mutate(self, info, fecha):
        facturas = FacturaModel.query.filter(FacturaModel.fecha == fecha).all()
        for factura in facturas:
            db.session.delete(factura)
        db.session.commit()

        return deleteFacturaPorFecha(facturas=facturas)

class deleteFacturaPorIdClienteFk(Mutation):
    class Arguments:
        id_cliente_fk = Int(required=True)

    facturas = List(lambda: Factura)

    def mutate(self, info, id_cliente_fk):
        facturas = FacturaModel.query.filter(FacturaModel.id_cliente_fk == id_cliente_fk).all()
        for factura in facturas:
            db.session.delete(factura)
        db.session.commit()

        return deleteFacturaPorIdClienteFk(facturas=facturas)
# FIN FACTURA-----

class Mutation(ObjectType):
    create_persona = createPersona.Field()
    update_persona = updatePersona.Field()
    delete_persona = deletePersona.Field()

    #agregado por mi
    create_Cliente = createCliente.Field()
    update_cliente = updateCliente.Field()
    delete_cliente = deleteCliente.Field()

    create_pasaporte = createPasaporte.Field()
    update_pasaporte = updatePasaporte.Field()
    delete_pasaporte = deletePasaporte.Field()

    create_factura = createFactura.Field()
    update_factura = updateFactura.Field()
    delete_factura = deleteFactura.Field()
    delete_facturaPorFecha = deleteFacturaPorFecha.Field()
    delete_facturaPorIdClienteFk = deleteFacturaPorIdClienteFk.Field()