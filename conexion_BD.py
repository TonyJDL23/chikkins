import psycopg2


def connection():
    connec = psycopg2.connect(
        host="localhost",
        user="TonyJDL23",
        password="Antony23",
        database="Restaurant_Chikkins",
    )
    print("Conexion Exitosa :)")
    return connec
