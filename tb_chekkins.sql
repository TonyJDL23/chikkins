-- CREATE TABLE--
CREATE TABLE IF NOT EXISTS Cliente(
	cedula int not NULL,
	nombre varchar (30),
	whatsapp varchar(13),
	email varchar(50),
	primary key(cedula)
)

CREATE TABLE IF NOT EXISTS Pedido(
	num_pedido int not NULL,
	cant_hambur int,
	monto_delivery decimal(2,2),
	total_pagar decimal (3,2),
	modo_pago varchar (10),
	sreen_pago bytea,
	status varchar (12),
	fecha_hora timestamp,
	ciudad varchar (15),
	municipio varchar(15),
	observacion text,
	ced_cliente int not NULL,
	primary key(num_pedido),
	foreign key (ced_cliente) references Cliente(cedula)
)