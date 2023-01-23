from typing import List
from connections import create_connection
import database


class Option:
    def __init__(self, option_text: str, poll_id: int, _id: int = None):
        self.id = _id
        self.text = option_text
        self.poll_id = poll_id

    def __repr__(self) -> str:
        return f"Option({self.text!r}, {self.poll_id!r}, {self.id!r})"

    def save(self):
        conn = create_connection()
        new_option_id = database.add_option(self.text, self.poll_id)
        conn.close()
        self.id = new_option_id

    @classmethod
    def get(cls, option_id: int) -> "Option":
        conn = create_connection()
        option = database.get_option(conn, option_id)
        conn.close()
        return cls(option[1], option[2], option[0])

    def vote(self, username: str):
        conn = create_connection()
        database.add_poll_vote(conn, username, self.id)
        conn.close()

    @property
    def votes(self) -> List[database.Vote]:
        conn = create_connection()
        votes = database.get_votes_for_option(conn, self.id)
        conn.close()
        return votes