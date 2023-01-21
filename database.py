import os
import psycopg2
from psycopg2.extras import execute_values
from dotenv import load_dotenv


load_dotenv()


CREATE_POLLS = open("./scripts/sql/ddl/create_table_polls.sql", 'r').read()
CREATE_OPTIONS = open("./scripts/sql/ddl/create_table_options.sql", 'r').read()
CREATE_VOTES = open("./scripts/sql/ddl/create_table_votes.sql", 'r').read()
SELECT_POLL_ALL = open("./scripts/sql/dql/select_poll_all.sql", 'r').read()
SELECT_POLL_LATEST = open("./scripts/sql/dql/select_poll_latest.sql", 'r').read()
SELECT_POLL_WITH_OPTIONS = open("./scripts/sql/dql/select_poll_with_options.sql", 'r').read()
SELECT_POLL_VOTE_DETAILS = open("./scripts/sql/dql/select_poll_vote_details.sql", 'r').read()
SELECT_RANDOM_VOTE = open("./scripts/sql/dql/select_vote_random.sql", 'r').read()
INSERT_OPTION = open("./scripts/sql/dml/insert_option.sql", 'r').read()
INSERT_VOTE = open("./scripts/sql/dml/insert_vote.sql", 'r').read()
INSERT_POLL_RETURN_ID = open("./scripts/sql/dml/insert_poll_return_id.sql", 'r').read()

conn = psycopg2.connect(os.environ["DATABASE_URI"])


def create_tables(conn):
    with conn:
        with conn.cursor() as curs:
            curs.execute(CREATE_POLLS)
            curs.execute(CREATE_OPTIONS)
            curs.execute(CREATE_VOTES)


def create_poll(conn, title, owner, options):
    with conn:
        with conn.cursor() as curs:
            curs.execute(INSERT_POLL_RETURN_ID, (title, owner))
            # curs.execute("""
            #     SELECT id FROM poll.polls ORDER BY id DESC LIMIT 1;
            # """)

            poll_id = curs.fetchone()[0]
            option_values = [(option_text, poll_id) for option_text in options]

            execute_values(curs, INSERT_OPTION, option_values)
            # for option_value in option_values:
            #     curs.execute(INSERT_OPTION, option_value)


def get_polls(conn):
    with conn:
        with conn.cursor() as curs:
            curs.execute(SELECT_POLL_ALL)

            return curs.fetchall()


def get_latest_polls(conn):
    with conn:
        with conn.cursor() as curs:
            curs.execute(SELECT_POLL_LATEST)

            return curs.fetchall()


def get_poll_details(conn, poll_id):
    with conn:
        with conn.cursor() as curs:
            curs.execute(SELECT_POLL_WITH_OPTIONS, (poll_id,))

            return curs.fetchall()


def get_poll_and_vote_results(conn, poll_id):
    with conn:
        with conn.cursor() as curs:
            curs.execute(SELECT_POLL_VOTE_DETAILS, (poll_id,))

            return curs.fetchall()


def get_random_poll_vote(conn, option_id):
    with conn:
        with conn.cursor() as curs:
            curs.execute(SELECT_RANDOM_VOTE, (option_id,))

            return curs.fetchone()


def add_poll_vote(conn, username, option_id):
    with conn:
        with conn.cursor() as curs:
            curs.execute(INSERT_VOTE, (username, option_id))
