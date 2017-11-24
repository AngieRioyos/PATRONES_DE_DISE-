"""MARIA DE LOS ANGELES RIOYOS HERRERA
************GITI9072-e*****************
####UNIDAD 3: PATRONES DE DISEÑO######"""

import psycopg2
from MARH_Config import config

def connect():
    """Connect to the Postgresql database server"""
    connection = None

    try:
        # Read connection parameters
        params = config()

        # Connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        connection = psycopg2.connect(**params)

        # Create cursor
        cursor = connection.cursor()

        # Execute a statement
        print('PostgreSQL database version:')
        cursor.execute('SELECT version()')

        # Dislay the PostgreSQL database server version
        db_version = cursor.fetchone()
        print(db_version)

        # Close the communication with the PostgreSQL
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('Database connection closed.')

if __name__ == '__main__':
    connect()




