CREATE TABLE persona (
	id serial PRIMARY KEY,
	name VARCHAR (50) NOT NULL,
	last_name VARCHAR (50) NOT NULL,
	email VARCHAR (150)
);

CREATE TABLE departamento (
	id serial PRIMARY KEY,
	name VARCHAR (50) NOT NULL,
	fk_persona integer,
	CONSTRAINT depto_frkey FOREIGN KEY (fk_persona) 
	REFERENCES persona (id)
);

alter table persona add column depto_fk int;	/*agregar un columna a una tabla*/
alter table persona add CONSTRAINT persona_frkey FOREIGN key (depto_fk) references departamento (id)	/*agregar una restriccion*/
update persona set depto_fk = valor where id = valor;	/*actualizar valor de una persona*/
alter table persona alter column depto_fk set not null;

INSERT INTO persona (name, last_name) VALUES ('Juan', 'Saldivia');	/*agregar un nuevo dato*/
INSERT INTO departamento (name, fk_persona) values ('compras', 1);

SELECT * FROM persona;

SELECT * FROM persona WHERE id = 2;

DELETE FROM persona WHERE id = 2;

UPDATE persona SET email = 'algo@algo.com' WHERE id = 15;

select * from departamento d join persona p on (d.fk_persona = p.id) where p.id =1;


mutation{	/*asi se crea un persona desde graphql*/
  createPersona(name: "Tito", lastName: "Ledesma", email: "asds@asd.asd"){
    persona{
      id
      name
      lastName
      email 
    }
  }
}

mutation{	/*asi se actualiza una persona desde graphql(lo busca opr su id)*/
  updatePersona(email:"marquitoss@gmail.com" personaId:3){
    persona{
      name
      lastName
      email
    }
  }
}

query{	/*asi se busca una persona desde graphql*/
  personas(id:2){
    name
    lastName
    email
  }
}
/*agregado por mi*/
CREATE TABLE cliente (id serial PRIMARY KEY,name VARCHAR (50) NOT NULL,last_name VARCHAR (50) NOT NULL,email VARCHAR (150));

CREATE TABLE pasaporte (id serial PRIMARY KEY,numero_pasaporte VARCHAR(255) NOT NULL,fecha_expiracion DATE NOT NULL,  cliente_id_fk INTEGER REFERENCES Cliente(id));  /*cliente_id_fk INTEGER REFERENCES Cliente(id) significa q el valor q se le vaya asignar a cliente_id_fk debe estar presente en la tabla Cliente(id)*/

CREATE TABLE Factura (id serial PRIMARY KEY,fecha DATE NOT NULL,monto DECIMAL(10, 2) NOT NULL,id_Cliente_fk INTEGER REFERENCES Cliente(id) NOT NULL);