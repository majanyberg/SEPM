import sqlite3
from storage import connect


def get_user() -> dict:
    with connect() as cur:
        query = "SELECT * FROM user_profile"
        cur.execute(query)
        results = cur.fetchall()


        user_profile = {}
        for result in results:
            user_profile[result["key"]] = result["value"]
        return user_profile
   
def create_user():
    pass

def delete_user():
    pass

def login():
    pass

def logout():
    pass

def update_user():
    pass

def get_user_stats():
    pass

def update_user_stats():
    pass