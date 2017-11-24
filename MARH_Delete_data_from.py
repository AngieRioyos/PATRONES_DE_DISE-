"""MARIA DE LOS ANGELES RIOYOS HERRERA
************GITI9072-e*****************
####UNIDAD 3: PATRONES DE DISEÑO######"""

import psycopg2
from MARH_Config import config

def delete_part(part_id):
    """Delete the table part by the part_id"""
    conn = None
    rows_deleted = 0
    try:
        # read the configuration of the database
        params = config()
        # connect to the Postgres database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # ejecutar la modificacion del statement
        cur.execute("DELETE FROM parts WHERE part_id = %s", (part_id,))
        # execute the statement modification
        rows_deleted = cur.rowcount
        # saves the changes in the database
        conn.commit()
        # closes the communication with the PostGres database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return rows_deleted