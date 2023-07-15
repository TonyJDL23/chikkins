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


if __name__ == "__main__":
    app.run(debug=True, port=4000)
