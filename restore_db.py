#!/usr/bin/python
import os
import psycopg2
from dotenv import load_dotenv


load_dotenv()


def drop_tables():

    conn = psycopg2.connect(os.environ["DATABASE_URI"])
    try:
        with conn:
            with conn.cursor() as curs:
                curs.execute('CALL poll.drop_tables()')

                # commit the transaction
                conn.commit()

                # close the cursor
                curs.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def create_tables():

    conn = psycopg2.connect(os.environ["DATABASE_URI"])
    try:
        with conn:
            with conn.cursor() as curs:
                curs.execute('CALL poll.create_tables()')

                # commit the transaction
                conn.commit()

                # close the cursor
                curs.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def populate_tables():

    conn = psycopg2.connect(os.environ["DATABASE_URI"])
    try:
        with conn:
            with conn.cursor() as curs:
                curs.execute('CALL poll.populate_tables()')

                # commit the transaction
                conn.commit()

                # close the cursor
                curs.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    drop_tables()
    create_tables()
    populate_tables()
