import psycopg2


def connection():
    connec = psycopg2.connect(
        host="localhost",
        user="TonyJDL23",
        password="Antony23",
        database="Restaurant_Chikkins",
        port=5432,
    )
    print("Conexion Exitosa :)")
    return connec
