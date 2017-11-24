"""MARIA DE LOS ANGELES RIOYOS HERRERA
************GITI9072-e*****************
####UNIDAD 3: PATRONES DE DISEÑO######"""

import psycopg2
from MARH_Config import config

def write_blob(part_id, path_to_file, file_extension):
    """Insert a BLOB into table"""
    con = None
    try:
        # Read image data
        drawing = open(path_to_file, 'rb').read()
        # Read the configuration of the Database
        params = config()
        # Connect to the PostgreSQL Database
        conn = psycopg2.connect(**params)
        # Create a new cursor
        cur = con.cursor()
        # execute the Insert statement
        cur.execute("INSERT INTO part_drawings,(part_id, file_extension, drawing_data)"
                    "VALUES (%s,%s,%s)",
                    (part_id, file_extension, psycopg2.Binary(drawing)))
        # Saves the changes in the database
        con.commit()
        # We close the communication with the database
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
