#!/usr/bin/python
from psycopg2.extras import execute_values
from dotenv import load_dotenv
from typing import List, Tuple


load_dotenv()


Poll = Tuple[int, str, str]
Vote = Tuple[str, int]
PollWithOption = Tuple[int, str, str, int, str, int]
PollResults = tuple[int, str, int, float]


# TODO: for below create views and query the views
SELECT_POLL = open("./scripts/sql/dql/select_poll.sql", 'r').read()
SELECT_POLL_ALL = open("./scripts/sql/dql/select_poll_all.sql", 'r').read()
SELECT_POLL_LATEST = open("./scripts/sql/dql/select_poll_latest.sql", 'r').read()
SELECT_POLL_WITH_OPTIONS = open("./scripts/sql/dql/select_poll_with_options.sql", 'r').read()
SELECT_POLL_VOTE_DETAILS = open("./scripts/sql/dql/select_poll_vote_details.sql", 'r').read()
SELECT_RANDOM_VOTE = open("./scripts/sql/dql/select_vote_random.sql", 'r').read()


# TODO: for below create stored procedures
INSERT_OPTION = open("./scripts/sql/dml/insert_option.sql", 'r').read()
INSERT_VOTE = open("./scripts/sql/dml/insert_vote.sql", 'r').read()
INSERT_POLL_RETURN_ID = open("./scripts/sql/dml/insert_poll_return_id.sql", 'r').read()


def create_tables(conn):
    with conn:
        with conn.cursor() as cur:
            cur.execute('CALL poll.create_tables()')

# -- polls --

def create_poll(conn, title, owner: str, options: List[str]) -> None:
    with conn:
        with conn.cursor() as cur:
            cur.execute(INSERT_POLL_RETURN_ID, (title, owner))
            poll_id = cur.fetchone()[0]
            option_values = [(option_text, poll_id) for option_text in options]
            execute_values(cur, INSERT_OPTION, option_values)


def get_polls(conn) -> List[Poll]:
    with conn:
        with conn.cursor() as cur:
            cur.execute(SELECT_POLL_ALL)
            return cur.fetchall()


def get_poll(conn, poll_id: int) -> Poll:
    with conn:
        with conn.cursor() as cur:
            cur.execute(SELECT_POLL, (poll_id,))
            return cur.fetchone()


def get_latest_polls(conn) -> List[PollWithOption]:
    with conn:
        with conn.cursor() as cur:
            cur.execute(SELECT_POLL_LATEST)
            return cur.fetchall()


def get_poll_details(conn, poll_id: int) -> List[PollWithOption]:
    with conn:
        with conn.cursor() as cur:
            cur.execute(SELECT_POLL_WITH_OPTIONS, (poll_id,))
            return cur.fetchall()


def get_poll_and_vote_results(conn, poll_id: int) -> List[PollResults]:
    with conn:
        with conn.cursor() as cur:
            cur.execute(SELECT_POLL_VOTE_DETAILS, (poll_id,))
            return cur.fetchall()


def get_random_poll_vote(conn, option_id: int) -> Vote:
    with conn:
        with conn.cursor() as cur:
            cur.execute(SELECT_RANDOM_VOTE, (option_id,))
            return cur.fetchone()


def add_poll_vote(conn, username: str, option_id: int) -> None:
    with conn:
        with conn.cursor() as cur:
            cur.execute(INSERT_VOTE, (username, option_id))
