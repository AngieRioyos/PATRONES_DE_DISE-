"""MARIA DE LOS ANGELES RIOYOS HERRERA
************GITI9072-e*****************
####UNIDAD 3: PATRONES DE DISEÑO######"""

import psycopg2
from MARH_Config import config

def create_tables():
    """create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE log(
        id SERIAL PRIMARY  KEY,
        ts TIMESTAMP NOT NULL,
        phrase VARCHAR (128) NOT NULL ,
        letters VARCHAR (32) NOT NULL ,
        ip VARCHAR (16) NOt NULL ,
        browser_string VARCHAR (256),
        results VARCHAR (64) NOT NULL 
        )
        """,
        """
        CREATE TABLE vendors(
        vendor_id SERIAL PRIMARY KEY ,
        vendor_name VARCHAR (255) NOT  NULL) 
        """,
        """
        CREATE TABLE parts(
        part_id SERIAL PRIMARY KEY,
        parts_name VARCHAR(255) NOT NULL
        ) 
        """,
        """
        CREATE TABLE parts_drawings(
        part_id INTEGER PRIMARY KEY,
        file_extension VARCHAR (5) NOT NULL,
        drawings_data BYTEA NOT  NULL,
        FOREIGN KEY(part_id)
        REFERENCES parts(part_id)
        ON UPDATE  CASCADE  ON DELETE CASCADE 
        )
        """,
        """
        CREATE TABLE vendor_parts(
        vendor_id INTEGER NOT NULL,
        part_id INTEGER NOT NULL, 
        PRIMARY KEY(vendor_id, part_id),
        FOREIGN KEY(vendor_id)
        REFERENCES vendors(vendor_id)
        ON UPDATE CASCADE ON DELETE CASCADE,
        FOREIGN KEY(part_id)
        REFERENCES parts(part_id)
        ON UPDATE CASCADE  ON DELETE CASCADE 
        )
        """,
    )

    connection = None
    try:
        # Read the connection parameters
        params = config()

        # Connect to the PostgreSQL server
        connection = psycopg2.connect(**params)
        cursor= connection.cursor()
        # Create table one by one
        for command in commands:
            cursor.execute(command)
        # Close communication with the PostgreSQL database server.
        cursor.close()

        #Commint the changes

        connection.commit()
    except (Exception, psycopg2.Database) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

if __name__== '__main__':
    create_tables()
