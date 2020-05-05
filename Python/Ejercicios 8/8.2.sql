drop database if exists agenda2;
create database agenda2;
use agenda2;


drop table if exists contacto;
create table contacto(
nombre varchar(50) not null,
telefono varchar(12) not null,
primary key (nombre)
);

drop table if exists grupo;
create table grupo(
nombre_p varchar(50) not null,
nombre_s varchar(50) not null,
Constraint fk_nombre_p
foreign key (nombre_p) 
references contacto (nombre) on delete cascade on update cascade,
Constraint fk_nombre_s
foreign key (nombre_s)
references contacto (nombre) on delete cascade on update cascade
);

insert into contacto values 
("arrieta","111111"),
("elio","222222"),
("benito","333333"),
("carlos","444444");

insert into grupo values
("arrieta","elio"),
("arrieta","benito"),
("benito","elio"),
("elio", "benito"),
("carlos", "arrieta"),
("arrieta", "carlos");

Select nombre, telefono, count(G.nombre_p) as 'grupo' From contacto C Left join grupo G On C.nombre = G.nombre_p Group by nombre;

Update contacto set nombre = "carlo", telefono = "123456" Where nombre = "carlos" and telefono = "444444";

delete from contacto where lower(nombre) = "carlos";