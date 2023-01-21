import os
import psycopg2


from dotenv import load_dotenv


load_dotenv()


CREATE_POLLS = open("./scripts/sql/ddl/create_table_polls.sql", 'r').read()
CREATE_OPTIONS = open("./scripts/sql/ddl/create_table_options.sql", 'r').read()
CREATE_VOTES = open("./scripts/sql/ddl/create_table_votes.sql", 'r').read()
SELECT_POLL_ALL = open("./scripts/sql/dql/select_poll_all.sql", 'r').read()
SELECT_POLL_WITH_OPTIONS = open("./scripts/sql/dql/select_poll_with_options.sql", 'r').read()
INSERT_OPTION = open("./scripts/sql/dml/insert_option.sql", 'r').read()
INSERT_VOTE = open("./scripts/sql/dml/insert_vote.sql", 'r').read()

conn = psycopg2.connect(os.environ["DATABASE_URI"])


def create_tables(conn):
    with conn:
        with conn.cursor() as curs:
            curs.execute(CREATE_POLLS)
            curs.execute(CREATE_OPTIONS)
            curs.execute(CREATE_VOTES)


def get_polls(conn):
    with conn:
        with conn.cursor() as curs:
            curs.execute(SELECT_POLL_ALL)

            return curs.fetchall()


def get_latest_polls(conn):
    with conn:
        with conn.cursor() as curs:
            pass


def get_poll_details(conn, poll_id):
    with conn:
        with conn.cursor() as curs:
            curs.execute(SELECT_POLL_WITH_OPTIONS, (poll_id,))

            return curs.fetchall()


def get_poll_and_vote_results(conn, poll_id):
    with conn:
        with conn.cursor() as curs:
            pass


def get_random_poll_vote(conn, option_id):
    with conn:
        with conn.cursor() as curs:
            pass


def create_poll(conn, title, owner, options):
    with conn:
        with conn.cursor() as curs:
            pass


def add_poll_vote(conn, username, option_id):
    with conn:
        with conn.cursor() as curs:
            curs.execute(INSERT_VOTE, (username, option_id))
