import os
import psycopg2

def showallMenu():
    DATABASE_URL = os.environ['DATABASE_URL']
    connection_db = psycopg2.connect(DATABASE_URL,sslmode='require')
    cursor = connection_db.cursor()
    SQL_cmd = f"""SELECT * FROM menu ;"""
    cursor.execute(SQL_cmd)
    connection_db.commit()
    raws = cursor.fetchall()
    data = []
    for raw in raws:
        data.append(raw)
    
    cursor.close()
    connection_db.close()
    return data

def addMenu(text):
    DATABASE_URL = os.environ['DATABASE_URL']
    connection_db = psycopg2.connect(DATABASE_URL,sslmode='require')
    cursor = connection_db.cursor()
    data = text.split(',')
    table_columns = '(menuname,menuprize)'
    SQL_cmd = f"""INSERT INTO menu { table_columns } VALUES(%s,%s);"""
    cursor.execute(SQL_cmd,(str(data[0]),int(data[1])))
    connection_db.commit()
    cursor.close()
    connection_db.close()
    return text