#!/usr/bin/python
from contextlib import contextmanager

from dotenv import load_dotenv
from typing import List, Tuple

load_dotenv()

Poll = Tuple[int, str, str]
Option = Tuple[int, str, str]
Vote = Tuple[str, int]
PollWithOption = Tuple[int, str, str, int, str, int]
# PollResults = tuple[int, str, int, float]


CALL_CREATE_TABLES = open("./scripts/sql/procedures/create_tables.sql", 'r').read()

# TODO: for below create views and query the views
SELECT_POLL = open("./scripts/sql/dql/select_poll.sql", 'r').read()
SELECT_OPTION = open("./scripts/sql/dql/select_option.sql", 'r').read()
SELECT_POLL_ALL = open("./scripts/sql/dql/select_poll_all.sql", 'r').read()
SELECT_POLL_LATEST = open("./scripts/sql/dql/select_poll_latest.sql", 'r').read()
SELECT_POLL_OPTIONS = open("./scripts/sql/dql/select_poll_options.sql", 'r').read()
# SELECT_POLL_VOTE_DETAILS = open("./scripts/sql/dql/select_poll_vote_details.sql", 'r').read()
# SELECT_VOTE_RANDOM = open("./scripts/sql/dql/select_vote_random.sql", 'r').read()
SELECT_VOTES_FOR_OPTION = open("./scripts/sql/dql/select_votes_for_option.sql", 'r').read()

# TODO: for below create stored procedures
INSERT_OPTION_RETURN_ID = open("scripts/sql/dml/insert_option_return_id.sql", 'r').read()
INSERT_VOTE = open("./scripts/sql/dml/insert_vote.sql", 'r').read()
INSERT_POLL_RETURN_ID = open("./scripts/sql/dml/insert_poll_return_id.sql", 'r').read()


@contextmanager
def get_cursor(conn):
    with conn:
        with conn.cursor() as cur:
            yield cur


def create_tables(conn):
    with get_cursor(conn) as cur:
        cur.execute(CALL_CREATE_TABLES)


def create_poll(conn, title, owner: str) -> None:
    with get_cursor(conn) as cur:
        cur.execute(INSERT_POLL_RETURN_ID, (title, owner))
        poll_id = cur.fetchone()[0]
        return poll_id


def get_polls(conn) -> List[Poll]:
    with get_cursor(conn) as cur:
        cur.execute(SELECT_POLL_ALL)
        return cur.fetchall()


def get_poll(conn, poll_id: int) -> Poll:
    with get_cursor(conn) as cur:
        cur.execute(SELECT_POLL, (poll_id,))
        return cur.fetchone()


def get_latest_poll(conn) -> Poll:
    with get_cursor(conn) as cur:
        cur.execute(SELECT_POLL_LATEST)
        return cur.fetchone()


def get_poll_options(conn, poll_id: int) -> List[Option]:
    with get_cursor(conn) as cur:
        cur.execute(SELECT_POLL_OPTIONS, (poll_id,))
        return cur.fetchall()


def get_option(conn, option_id: int) -> Option:
    with get_cursor(conn) as cur:
        cur.execute(SELECT_OPTION, (option_id,))
        return cur.fetchone()


def add_option(conn, option_text: str, poll_id: int):
    with get_cursor(conn) as cur:
        cur.execute(INSERT_OPTION_RETURN_ID, (option_text, poll_id))
        option_id = cur.fetchone()[0]
        return option_id


def get_votes_for_option(conn, option_id: int) -> List[Vote]:
    with get_cursor(conn) as cur:
        cur.execute(SELECT_VOTES_FOR_OPTION, (option_id,))
        return cur.fetchall()


def add_poll_vote(conn, username: str, option_id: int, vote_timestamp: float) -> None:
    with get_cursor(conn) as cur:
        cur.execute(INSERT_VOTE, (username, option_id, vote_timestamp))
