"""MARIA DE LOS ANGELES RIOYOS HERRERA
************GITI9072-e*****************
####UNIDAD 3: PATRONES DE DISEÑO######"""

import psycopg2
from MARH_Config import config


def update_vendor(vendor_id, vendor_name):
    """update provider name based on provider id"""

    sql = """UPDATE vendors 
              SET vendor_name = %s
              WHERE vendor_id = %s"""
    conn = None
    updated_rows = 0
    try:
        # read the base configuration
        params = config()
        # connect to the PostgreSQL Database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cursor = conn.cursor()
        # execute the UPDATE statement
        cursor.execute(sql, (vendor_name, vendor_id))
        # get the number of rows updated
        updated_rows = cursor.rowcount
        # Confirm or save the changes in the Database
        conn.commit()
        # Close the communication with the PostgreSQL Database
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows



