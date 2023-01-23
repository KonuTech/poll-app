from typing import List
from connection_pool import get_connection
from models.option import Option
import database


class Poll:
    def __init__(self, title: str, owner: str, _id: int = None):
        self.id = _id
        self.title = title
        self.owner = owner

    def __repr__(self):
        return f"Poll({self.name!r}, {self.id!r})"  # Poll('title', 'owner', 1)

    def save(self):
        with get_connection() as conn:
            new_poll_id = database.create_poll(conn, self.title, self.owner)
            self.id = new_poll_id

    def add_option(self, option_text: str):
        Option(option_text, self.id).save()

    @property
    def options(self) -> List[Option]:
        with get_connection() as conn:
            options = database.get_poll_options(conn, self.id)
            return [Option(option[1], option[2], option[0]) for option in options]

    @classmethod
    def get(cls, poll_id: int) -> "Poll":
        with get_connection() as conn:
            poll = database.get_poll(conn, poll_id)
            return cls(poll[1], poll[2], poll[0])

    @classmethod
    def all(cls) -> List["Poll"]:
        with get_connection() as conn:
            polls = database.get_polls(conn)
            return [cls(poll[1], poll[2], poll[0]) for poll in polls]

    @classmethod
    def latest(cls) -> "Poll":
        with get_connection() as conn:
            poll = database.get_latest_poll(conn)
            return cls(poll[1], poll[2], poll[0])
