import os
import datetime
import pytz
import psycopg2
from dotenv import load_dotenv


load_dotenv()


conn = psycopg2.connect(os.environ.get("DATABASE_URI"))

user_timezone = pytz.timezone("Europe/London")
new_post_content = input("Enter what you learned today: ")
new_post_date = user_timezone.localize(datetime.datetime.now())
utc_post_date = new_post_date.astimezone(pytz.utc)

with conn:
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO poll.posts(conten, date) VALUES (%s, %s)", (new_post_content, utc_post_date.timestamp())
        )


with conn:
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM posts;")
        for post in cur:
            _id, content, timestamp = post
            naive_datetime = datetime.datetime.utcfromtimestamp(timestamp)
            utc_date = pytz.utc.localize(naive_datetime)
            local_date = utc_date.astimezone(user_timezone)
            print(local_date)
            print(content)

