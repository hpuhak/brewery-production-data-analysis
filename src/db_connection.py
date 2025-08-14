import psycopg2
import pandas as pd

def get_connection():
    return psycopg2.connect(
        dbname="brewery_db",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )

def query_to_df(query):
    # Ajaa SQL-kyselyn ja palauttaa tuloksen Pandas DataFramena
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df
