"""MARIA DE LOS ANGELES RIOYOS HERRERA
************GITI9072-e*****************
####UNIDAD 3: PATRONES DE DISEÑO######"""

import psycopg2
from MARH_Config import config

def get_parts(vendor_id):
    "" "Obtain parts provided by a provider specified by the provider_id" ""
    conn = None
    try:
        # read the configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # another way to call a stored procedure
        # cur.execute ("SELECT * FROM get_parts_by_vendor (% s);", (vendor_id,))
        cur.callproc('get_parts_by_vendor', (vendor_id,))
        # set the result process
        row = cur.fetchone()
        while row is not None:
            print(row)
            row = cur.fetchone()
        # close the communication with the PostgreSQL database
            cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()