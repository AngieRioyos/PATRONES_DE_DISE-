"""MARIA DE LOS ANGELES RIOYOS HERRERA
************GITI9072-e*****************
####UNIDAD 3: PATRONES DE DISEÑO######"""

import psycopg2
from MARH_Config import config

def insert_vendor(vendor_name):
    """inserts a new vendor in the vendor table"""
    sql = """INSERT INTO vendors(vendor_name)
             VALUES(%s) RETURNING vendor_id;"""
    conn = None
    vendor_id = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL Database
        conn = psycopg2.connect(**params)
        # Create a new Cursor
        cur = conn.cursor()
        # execute the INSERT instruction
        cur.execute(sql, (vendor_name,))
        # retrieve the generated id
        vendor_id = cur.fetchone()[0]
        # commit changes to the Database
        conn.commit()
        # Close the communication with the Database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return vendor_id
