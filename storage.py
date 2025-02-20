import contextlib
import sqlite3

@contextlib.contextmanager
def connect():
    conn = sqlite3.connect('backend.db')
    cur = conn.cursor()
    try:
        yield cur
    finally:
        conn.close()

def get_words(category: str, difficulty: int, count=5) -> list:
    with connect() as cur:
        query = "SELECT * FROM words WHERE category = ? and difficulty = ? ORDER BY RANDOM() LIMIT ?"
        cur.execute(query, (category, difficulty, count))
        results = cur.fetchall()

        words = []
        for result in results:
            words.append({
                "swedish": result["swedish"],
                "english": result["english"],
            })
        return words

def get_times(difficulty: str, count=5) -> list:
    with connect() as cur:
        query = "SELECT * FROM times WHERE difficulty = ? ORDER BY RANDOM() LIMIT ?"
        cur.execute(query, (difficulty, count))
        results = cur.fetchall()

        words = []
        for result in results:
            words.append({
                "time": result["time"],
                "swedish": result["swedish"],
            })
        return words

def get_user_profile() -> dict:
    with connect() as cur:
        query = "SELECT * FROM user_profile"
        cur.execute(query)
        results = cur.fetchall()

        user_profile = {}
        for result in results:
            user_profile[result["key"]] = result["value"]
        return user_profile




