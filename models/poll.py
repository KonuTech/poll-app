from typing import List
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
        conn = create_connection()
        new_poll_id = database.create_poll(conn, self.title, self.owner)
        conn.cloe()
        self.id = new_poll_id

    def add_option(self, option_text: str):
        Option(option_text, self.id).save()

    def option(self) -> List[Option]:
        conn = create_connection()
        options = database.get_poll_options(conn, self.id)
        conn.close()
        return [Option(option[1], option[2], option[0]) for option in options]

    @classmethod
    def get(cls, poll_id: int) -> "Poll":
        conn = create_connection()
        poll = database.get_poll(conn, poll_id)
        conn.close()
        return cls(poll[1], poll[2], poll[0])

    @classmethod
    def all(cls) -> List["Poll"]:
        conn = create_connection()
        polls = database.get_polls(conn)
        conn.close()
        return [cls(poll[1], poll[2], poll[0]) for poll in polls]

    @classmethod
    def latest(cls) -> "Poll":
        conn = create_connection()
        poll = database.get_latest_polls()
        conn.close()
        return cls(poll[1], poll[2], poll[0])
