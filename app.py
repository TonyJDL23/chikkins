from flask import Flask, jsonify, request
from psycopg2 import extras
from conexion_BD import connection

app = Flask(__name__)


@app.route("/customers", methods=["POST"])
def customers():
    new_cliente = request.get_json()
    nombre = new_cliente["name"]
    whatsapp = new_cliente["whatsapp"]
    cedula = new_cliente["cedula"]
    email = new_cliente["email"]
    con = connection()
    cur = con.cursor()
    cur.execute(
        "INSERT INTO Cliente (cedula,nombre,whatsapp,email) VAlUES (%s,%s,%s,%s) ",
        (cedula, nombre, whatsapp, email),
    )
    con.commit()

    cur.close()
    con.close()
    return "create"


@app.route("/customers", methods=["GET"])
def lis_customers():
    con = connection()
    cur = con.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute("SELECT * FROM Cliente")
    clie = cur.fetchall()

    cur.close()
    con.close()
    return jsonify(clie)


@app.route("/customers/<cedula>", methods=["PUT"])
def update_customers(cedula):
    con = connection()
    cur = con.cursor(cursor_factory=extras.RealDictCursor)

    new_cliente = request.get_json()
    nombre = new_cliente["name"]
    whatsapp = new_cliente["whatsapp"]
    email = new_cliente["email"]

    cur.execute(
        "UPDATE Cliente SET nombre = %s, whatsapp = %s, email = %s where cedula= %s RETURNING * ",
        (nombre, whatsapp, email, cedula),
    )
    new_cliente = cur.fetchone()

    con.commit()

    cur.close()
    con.close()

    if new_cliente is None:
        return jsonify({"message": "Customers not found"})

    return "UPDATE"


@app.route("/orders", methods=["POST"])
def orders():
    new_order = request.get_json()
    cant_hambur = new_order["quanty"]
    modo_pago = new_order["paymet_method"]
    observacion = new_order["remark"]
    ciudad = new_order["city"]
    municipio = new_order["municipality"]
    cedula = new_order["cedula"]
    con = connection()
    cur = con.cursor(cursor_factory=extras.RealDictCursor)
    cur.execute(
        "INSERT INTO Pedido (cant_hambur,modo_pago,observacion,ciudad,municipio,ced_cliente) VAlUES (%s,%s,%s,%s,%s,%s)  RETURNING * ",
        (cant_hambur, modo_pago, observacion, ciudad, municipio, cedula),
    )
    order = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return jsonify(order)


if __name__ == "__main__":
    app.run(debug=True, port=4000)
