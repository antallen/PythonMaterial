import os
import psycopg2

def showallMenu():
    DATABASE_URL = os.environ['DATABASE_URL']
    connection_db = psycopg2.connect(DATABASE_URL,sslmode='require')
    cursor = connection_db.cursor()
    SQL_cmd = f"""SELECT * FROM menu ;"""
    cursor.execute(SQL_cmd)
    raws = cursor.fetchall()
    data = []
    for raw in raws:
        data.append(raw)

    return data