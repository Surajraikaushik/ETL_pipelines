# POSTgres SQL connection

import psycopg2

def db_conn():
    conn = psycopg2.connect(database="Sample_Data", user="postgres", password="Abhi@123", host="127.0.0.1", port="5432")
    print("Database Connected....")
    cur = conn.cursor()
    return cur
