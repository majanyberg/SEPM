import contextlib
import sqlite3

@contextlib.contextmanager
def connect():
    conn = sqlite3.connect('backend.db')
    cur = conn.cursor()
    try:
        yield cur
    finally:
        conn.commit()
        conn.close()

def get_words(category: str, difficulty: str, count=5) -> list:
    """ Gets <count> words of the given category and difficulty """
    with connect() as cur:
        query = "SELECT swedish, english, hint1, hint2, hint3 FROM words WHERE category = ? and difficulty = ? ORDER BY RANDOM() LIMIT ?"
        cur.execute(query, (category, difficulty, count))
        results = cur.fetchall()

        words = []
        for result in results:
            words.append({
                "swedish": result[0],
                "english": result[1],
                "hints": [
                    result[2],
                    result[3],
                    result[4],
                ]
            })
        return words

def get_times(difficulty: str, count=5) -> list:
    """ Gets <count> times of the given difficulty """
    with connect() as cur:
        query = "SELECT time, swedish FROM times WHERE difficulty = ? ORDER BY RANDOM() LIMIT ?"
        cur.execute(query, (difficulty, count))
        results = cur.fetchall()

        words = []
        for result in results:
            words.append({
                "time": result[0],
                "swedish": result[1],
            })
        return words

def get_user_profile(username: str) -> dict:
    """ Get the user profile for the given user """
    with connect() as cur:
        query = "SELECT key, value FROM user_profile WHERE username = ?"
        cur.execute(query, (username,))
        results = cur.fetchall()

        user_profile = {}
        for result in results:
            user_profile[result[0]] = result[1]
        return user_profile


def update_user_profile(username: str, user_profile: dict):
    """ Updates the user profile for given user with the given key-value pairs"""
    with connect() as cur:
        # First delete existing values for profile
        query = "DELETE FROM user_profile WHERE username = ?"
        cur.execute(query, (username,))
        params = []
        for key, value in user_profile.items():
            params.append((username, key, value))
        query = "INSERT INTO user_profile (username, key, value) VALUES (?, ?, ?)"
        cur.executemany(query, params)
