from flask import Flask, jsonify, request, render_template
from psycopg2 import extras
from conexion_BD import connection
from werkzeug.utils import secure_filename
import datetime
import os
from os import path

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
    prec_hamb = 5
    new_order = request.get_json()
    cant_hambur = new_order["quanty"]
    modo_pago = new_order["paymet_method"]
    observacion = new_order["remark"]
    ciudad = new_order["city"]
    municipio = new_order["municipality"]
    cedula = new_order["cedula"]
    con = connection()
    cur = con.cursor(cursor_factory=extras.RealDictCursor)

    if municipio != "maneiro":
        monto_delivery = 2.00
    else:
        monto_delivery = 0.00

    total = (int(cant_hambur) * prec_hamb) + monto_delivery

    fe_ho_actu = datetime.datetime.now()
    fecha_hora = datetime.datetime.strftime(fe_ho_actu, "%d-%m-%Y %H:%M:%S")
    print(fecha_hora)
    cur.execute(
        "INSERT INTO Pedido (cant_hambur,modo_pago,observacion,ciudad,municipio,monto_delivery,total_pagar,fecha_hora,ced_cliente ) VAlUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING *",
        (
            cant_hambur,
            modo_pago,
            observacion,
            ciudad,
            municipio,
            monto_delivery,
            total,
            fecha_hora,
            cedula,
        ),
    )

    order = cur.fetchone()
    con.commit()
    cur.close()
    con.close()
    return jsonify(order)


@app.route("/enviar-screenshot", methods=["GET"])
def enviar_screenshot():
    return render_template("payment-screenshot.html")


# se crea la configuracion para guaradar las imagenes
app.config["UPLOAD_IMAG"] = "screenshot"  # la ruta donde se va a guardar la imagen

ALLOWED_EXTENSIONS = set(["png", "jpg"])  # las extensiones permitidas


def allowed_file(file):
    file = file.split(".")
    if file[1] in ALLOWED_EXTENSIONS:
        return True
    return False


@app.route("/orders/<id>/payment-screenshot", methods=["POST"])
def payment_screenshot(id):
    file = request.files["screenshot"]
    filename = secure_filename(file.filename)  # type: ignore

    if file and allowed_file(filename):
        print("permitido")
        extension = path.splitext(filename)[1]
        new_name = id + extension
        file.save(os.path.join(app.config["UPLOAD_IMAG"], new_name))
        # ahora se guarda en la BD
        con = connection()
        cur = con.cursor(cursor_factory=extras.RealDictCursor)
        cur.execute(
            "UPDATE Pedido SET sreen_pago = %s where num_pedido= %s",
            (new_name, id),
        )

        con.commit()

        cur.close()
        con.close()
        return new_name
    else:
        return jsonify({"message": "No se logro guardar la imagen"})


@app.route("/orders/<id>/status", methods=["PATCH"])
def update_status(id):
    con = connection()
    cur = con.cursor(cursor_factory=extras.RealDictCursor)

    new_status = request.get_json()
    estado = new_status["status"]

    cur.execute(
        "UPDATE Pedido SET status = %s where num_pedido= %s RETURNING *",
        (estado, id),
    )
    update_excelent = cur.fetchone()

    con.commit()

    cur.close()
    con.close()

    if update_excelent is None:
        return jsonify({"message": "NO SE LOGRO ACTUALIZAR"})

    return jsonify({"message": "ACTUALIZACION EXITOSA"})


if __name__ == "__main__":
    app.run(debug=True, port=4000)
