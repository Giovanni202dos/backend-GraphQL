from graphene import (
    ObjectType,
    Field,
    String,
    Boolean,
    List,
    Int,
    Date,
    Float
)

from .persona import Persona as PersonaModel
from .objects import Persona, Departamento
from .departamento import Departamento as DepartamentoModel

#agregado por mi
from .cliente import Cliente as ClienteModel
from .objects import Cliente, Pasaporte, Factura
from .pasaporte import Pasaporte as PasaporteModel
from .factura import Factura as FacturaModel

class Query(ObjectType):
    personas = List(lambda: Persona, last_name=String(), id=Int(), has_email=Boolean(), order_by_name=Boolean())    #lo que se muestra en la pagina graphQL(son los arguemtos q se le pasa para que bussque)
    departamentos = List(lambda: Departamento)  #lo que se muestra en la pagina graphQL
    departamento = Field(lambda: Departamento, id=Int())    #lo que se muestra en la pagina graphQL

    #agregado por mi    (los nombres de los resolve deben coincidir con estos)
    clientes = List(lambda: Cliente,name=String(), last_name=String(), id=Int(), has_email=Boolean(), order_by_name=Boolean())
    cliente = Field(lambda: Cliente, id=Int())
    cliente_por_last_name = List(lambda: Cliente, last_name=String())   #duelve una lista de apellidos que coincidan
    cliente_por_email = Field(lambda: Cliente, email=String())   #duelve un cliente por el email
    pasaportes = List(lambda: Pasaporte, id=Int())   #duelve un Pasaporte o muchos si no le ingresa un id
    pasaporte = Field(lambda: Pasaporte, numero_pasaporte=String())   #duelve un Pasaporte por el numero_pasaporte
    pasaporteIdCliente = Field(lambda: Pasaporte, cliente_id_fk=Int())   #duelve un Pasaporte por el id del cliente
    facturas = List(lambda: Factura)   #duelve una lista de facturas
    factura_por_id = Field(lambda: Factura, id=Int())   #duelve una factura por su id
    facturas_por_fecha = List(lambda: Factura, fecha=Date())   #duelve una lista de facturas por la fecha
    facturas_excede_monto = List(lambda: Factura, monto=Float())    #devuelve una lista de facturas que exceden el monto ingresado
    
    ####---
    def resolve_personas(self, info, id=None, last_name=None, has_email=None, order_by_name=None):  #filtrado general
        query = Persona.get_query(info=info)
        if id:
            query = query.filter(PersonaModel.id==id)
        if last_name:
            query = query.filter(PersonaModel.last_name==last_name)
        if has_email is not None:
            if has_email:
                query = query.filter(PersonaModel.email != None)
            else:
                query = query.filter(PersonaModel.email == None)
        if order_by_name:
            query = query.order_by(PersonaModel.name)
        return query.all()
    
    def resolve_departamentos(self, info):
        query = Departamento.get_query(info=info)
        return query.all()
    
    def resolve_departamento(self, info, id):
        dpto = DepartamentoModel.query.get(id)
        return dpto
    
    #agregado por mi
    def resolve_clientes(self, info, id=None, name=None,last_name=None, has_email=None, order_by_name=None):  #filtrado general
        query = Cliente.get_query(info=info)
        if id:
            query = query.filter(ClienteModel.id==id)
        if name:
            query = query.filter(ClienteModel.name==name)
        if last_name:
            query = query.filter(ClienteModel.last_name==last_name)
        if has_email is not None:
            if has_email:
                query = query.filter(ClienteModel.email != None)
            else:
                query = query.filter(ClienteModel.email == None)
        if order_by_name:
            query = query.order_by(ClienteModel.name)
        return query.all()

    def resolve_cliente(self, info, id):
        cliente = ClienteModel.query.get(id)    #query.get busca por la primaria key
        return cliente

    def resolve_cliente_por_last_name(self, info, last_name):
        cliente = ClienteModel.query.filter(ClienteModel.last_name == last_name).all()  #all() significa que devuelve una lista de clientes q coincidan(si pongo first()devolveria el primero que coincida y no seria una lista)
        return cliente
    
    def resolve_cliente_por_email(self, info, email):
        cliente = ClienteModel.query.filter(ClienteModel.email == email).first()  #.firts()devolveria el primero que coincida y no seria una lista)
        return cliente
    
    def resolve_pasaportes(self, info, id=None):
        query = Pasaporte.get_query(info=info)
        if id:
            query = query.filter(PasaporteModel.id==id)
            return query
        else:
            return query.all()

    def resolve_pasaporte(self, info, numero_pasaporte):
        pasaporte = PasaporteModel.query.filter(PasaporteModel.numero_pasaporte == numero_pasaporte).first()  #.firts()devolveria el primero que coincida y no seria una lista)
        return pasaporte

    def resolve_pasaporteIdCliente(self, info, cliente_id_fk):
        pasaporte = PasaporteModel.query.filter(PasaporteModel.cliente_id_fk == cliente_id_fk).first()  #.firts()devolveria el primero que coincida y no seria una lista)
        return pasaporte

    def resolve_facturas(self, info):
        query = Factura.get_query(info=info)
        return query.all()

    def resolve_factura_por_id(self, info, id):
        factura = FacturaModel.query.get(id)
        return factura

    def resolve_facturas_por_fecha(self, info, fecha):
        facturas = FacturaModel.query.filter(FacturaModel.fecha == fecha).all()  #all() significa que devuelve una lista de clientes q coincidan(si pongo first()devolveria el primero que coincida y no seria una lista)
        return facturas
    
    def resolve_facturas_excede_monto(self, info, monto):
        facturas = FacturaModel.query.filter(FacturaModel.monto>monto).all()
        return facturas