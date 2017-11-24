"""MARIA DE LOS ANGELES RIOYOS HERRERA
************GITI9072-e*****************
####UNIDAD 3: PATRONES DE DISEÑO######"""

import psycopg2
from MARH_Config import config

def add_part(part_name, vendor_list):
    # execute the statement statement of a new row in the table parts
    inser_part = "INSERT INTO parts(part_name) VALUES  (%s) RETURNING part_id;"
    # execute the statement statement of a new row in the table parts
    assign_vendor = "INSERT INTO vendor_parts(vendor_id, part_id) VALUES (%s, %s)"

    conn = None
    try:
        # read the configuration of the database
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new course
        cur = conn.cursor()
        # insertar una nueva parte
        cur.execute(insert_part, (part_name,))
        # obtener el id_part
        part_id = cur.fetchone()[0]
        # assign parts provided by suppliers
        for vendor_id in vendor_list:
            cur.execute(assign_vendor, (vendor_id, part_id))

        # save Changes
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
