from graphene_sqlalchemy import (
    SQLAlchemyObjectType,
)
from graphene import (
    # Int
    String
)
from models.departamento import Departamento as DepartamentoModel
# from models.user import User as UserModel
from models.persona import Persona as PersonaModel

#agregado por mi
from models.cliente import Cliente as ClienteModel
from models.pasaporte import Pasaporte as PasaporteModel
from models.factura import Factura as FacturaModel

class Persona(SQLAlchemyObjectType):
    class Meta:
        model = PersonaModel
    name = String(description='representa el nombre de la persona')

class Departamento(SQLAlchemyObjectType):
    class Meta:
        model = DepartamentoModel
        # exclude_fields = ('fk_persona')

#agregado por mi
class Cliente(SQLAlchemyObjectType):
    class Meta:
        model = ClienteModel

class Pasaporte(SQLAlchemyObjectType):
    class Meta:
        model = PasaporteModel

class Factura(SQLAlchemyObjectType):
    class Meta:
        model = FacturaModel

# class User(SQLAlchemyObjectType):
#     class Meta:
#         model = UserModel