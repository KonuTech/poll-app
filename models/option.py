import datetime
from typing import List
import pytz

from connection_pool import get_connection
import database


class Option:
    def __init__(self, option_text: str, poll_id: int, _id: int = None):
        self.id = _id
        self.text = option_text
        self.poll_id = poll_id

    def __repr__(self) -> str:
        return f"Option({self.text!r}, {self.poll_id!r}, {self.id!r})"

    def save(self):
        with get_connection() as conn:
            new_option_id = database.add_option(conn, self.text, self.poll_id)
            self.id = new_option_id

    @classmethod
    def get(cls, option_id: int) -> "Option":
        with get_connection() as conn:
            option = database.get_option(conn, option_id)
            return cls(option[1], option[2], option[0])

    def vote(self, username: str):
        current_datetime_utc = datetime.datetime.now(tz=pytz.utc)
        current_timestamp = current_datetime_utc.timestamp()
        with get_connection() as connection:
            database.add_poll_vote(connection, username, current_timestamp, self.id)

    @property
    def votes(self) -> List[database.Vote]:
        with get_connection() as conn:
            votes = database.get_votes_for_option(conn, self.id)
            return votes
