from integration_backend import content
import sqlite3
from datetime import datetime
import json
from integration_backend.user_management import _connect, _get_table_columns

def get_words(category: str, difficulty: str, count=5) -> list:
    """
    get_words
    Fetch a specified amount of word/answer pairs of the specified category from the database.
    Args:
        category (str): The category of the words.
        difficulty (str): The difficulty level of the words. Difficulties are 'easy', 'medium', and 'hard'.
        count (int): The number of words to fetch. The maximum count per difficulty and category is 20.
    Returns:
        list: A list of dictionaries containing word/answer pairs and a list of three hints. 
        For example:
        [
            {"swedish": "hej", "english": "hello", "hints": ["first hint", "second hint", "third hint"]},
            {"swedish": "tack", "english": "thanks", "hints": ["first hint", "second hint", "third hint"]},
            ...
        ]
    """
    return content.get_words(category, difficulty, count)


def get_times(difficulty: str, count=5) -> list:
    """
    get_times
    Fetch a specified amount of digital time/swedish answer pairs from the database.
    Args:
        difficulty (str): The difficulty level of the times. Difficulties are 'easy', 'medium', and 'hard'.
        count (int): The number of times to fetch. The maximum count is 96.
    Returns:
        list: A list of dictionaries containing digital time/swedish answer pairs. 
        For example:
        [
            {"time": "1:15", "swedish": "kvart över ett"},
            {"time": "1:30", "swedish": "halv två"},
            ...
        ]
    """
    return content.get_times(difficulty, count)

def update_score(username: str, score: int) -> None:
    """
    update_score
    Update the score of a user.
    Args:
        username (str): username of the user
        score (int): score to add
    Returns:
        None
    """
    content.update_score(username, score)



###########################################################
##################### User Management #####################
###########################################################


def get_user(username: str) -> dict:
    """
    Retrieves all user information from the database.
    Args:
        username (str): The username of the user to fetch.
    Returns:
        dict: User details as a dictionary if found, else an empty dictionary.
    """
    try: 
        conn = _connect()  
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

        query = "SELECT * FROM users WHERE username = ?"
        cur.execute(query, (username,))
        
        row = cur.fetchone()
        conn.close()

        return dict(row) if row else {}
    
    except Exception as e:
        print(f"Unexpected error: {e}")
        return {}
   
def create_user(username: str, real_name: str = None, age: int = 0, 
                country: str = None, user_type: str = None, 
                total_time: int = 0, words_learned: int = 0) -> None:
    """
    Creates a new user entry in the database.
    Args:
        username (str): The username.
        real_name (str, optional): The real name of the user.
        age (int, optional): The age of the user. Defaults to 0.
        country (str, optional): The country of the user.
        user_type (str, optional): The type of user.
        total_time (int, optional): Total time spent in minutes. Defaults to 0.
        words_learned (int, optional): Number of words learned. Defaults to 0.
    """
    try: 
        conn = _connect()
        cur = conn.cursor()

        query = """INSERT INTO users (username, real_name, age, country, user_type, total_time, words_learned)
        VALUES (?, ?, ?, ?, ?, ?, ?)"""
        cur.execute(query, (username, real_name, age, country, user_type, total_time, words_learned))

        conn.commit()  
        conn.close()

    except Exception as e:
        print(f"Unexpected error: {e}")
        return {}

def delete_user(username: str) -> None:
    """
    Deletes a user from the database.
    Args:
        username (str): The username of the user to delete.
    """
    try: 
        conn = _connect()
        cur = conn.cursor()

        query = "DELETE FROM users WHERE username = ?"
        cur.execute(query, (username,))

        conn.commit()  
        conn.close()
    except Exception as e:
        print(f"Unexpected error: {e}")
        return {}


class SessionManager:
    """
    Manages user login sessions.
    """
    def __init__(self):
        self._current_user = None
        self._login_time = None

    def login(self, username: str) -> str:
        """
        Logs in a user and tracks session start time.
        Args:
            username (str): The username of the user logging in.
        Returns:
            str: The username of the logged-in user, or None if login fails.
        """
        try:
            user = get_user(username)
            if user:
                self._current_user = user['username']
                self._login_time = datetime.now()
                print(f"{username} logged in at {self._login_time}.")
            else:
                print(f"Error: user {username} not found.")
            return self._current_user
        except Exception as e:
            print(f"Unexpected error during login: {e}")
            return None

    def logout(self) -> None:
        """
        Logs out the current user and updates total time spent.
        """
        try: 
            if self._current_user and self._login_time:
                elapsed = datetime.now() - self._login_time
                minutes_spent = elapsed.total_seconds() / 60
                prev_time = get_user(self._current_user)['total_time']
                if  not prev_time:
                    prev_time = 0
                update_cur_user('total_time', prev_time + minutes_spent)
            self._current_user = None
        
        except Exception as e:
            print(f"Unexpected error during logout: {e}")
            return None

    def get_current_user(self) -> str:
        """
        Returns the currently logged-in user.
        Returns:
            str: The username of the logged-in user, or None if no user is logged in.
        """
        return self._current_user

# The game modules can import session_manager and call i.e. session_manager.login()
session_manager = SessionManager()


def update_cur_user(column: str, value) -> None:
    """
    Updates a specific entry in the current logged-in user's database record.
    Args:
        column (str): The column to update.
        value: The new value for the column.
    """
    try: 
        current_user = session_manager.get_current_user()
        
        if current_user is None:
            print("Error: Cannot update current user because no user is logged in.")
            return
        
        if column not in _get_table_columns("users"):
            print(f"Error: Invalid column name \"{column}\"")
            return
        
        query = f"UPDATE users SET {column} = ? WHERE username = ?"
        
        conn = _connect()
        cur = conn.cursor()

        cur.execute(query, (value, current_user))

        conn.commit()
        conn.close()
    
    except Exception as e:
        print(f"Unexpected error: {e}")
        return {}


def get_cur_user_stats() -> dict:
    """
    Retrieves statistics of the currently logged-in user.
    Returns:
        dict: A dictionary containing 'total_time' and 'words_learned' statistics.
    """
    try:
        current_user = session_manager.get_current_user()
        
        if current_user is None:
            print("Error: No user is logged in")
            return
        
        query = "SELECT total_time, words_learned FROM users WHERE username = ?"

        conn = _connect()
        cur = conn.cursor()

        cur.execute(query,(current_user,))
        result = cur.fetchone()

        if result is None:
            print("Error: No statistics found for the current user.")
            conn.close()
            return

        # Create a dictionary with column names as keys and the corresponding values
        stats = {
            'total_time': result[0],
            'words_learned': result[1]
        }
        conn.close()
        return stats
    
    except Exception as e:
        print(f"Unexpected error: {e}")
        return {}

def increase_words_learned(value: int) -> None:
    """
    Increases the words learned stat for the logged-in user.
    Args:
        value (int): The number of words to add.
    """
    try: 
        current_user = session_manager.get_current_user()
        
        if current_user is None:
            print("Error: Cannot update current user because no user is logged in.")
            return
        
        old_value = get_user(current_user)["words_learned"]
        if not old_value:
            old_value = 0
        value = old_value + value
        
        query = f"UPDATE users SET words_learned = ? WHERE username = ?"
        
        conn = _connect()
        cur = conn.cursor()

        cur.execute(query, (value, current_user))

        conn.commit()
        conn.close()
    
    except Exception as e:
        print(f"Unexpected error: {e}")
        return {}

def get_words_learned() -> int:
    """
    Retrieves the words learned stat of the logged-in user.
    Returns:
        int: The number of words learned, or 0 if no user is logged in.
    """
    try: 
        cur_user = session_manager.get_current_user()
        if not cur_user:
            print("Error: No user is logged in")
            return 0
        else: 
            return get_user(session_manager.get_current_user())["words_learned"]
    
    except Exception as e:
        print(f"Unexpected error: {e}")
        return {}
    

def store_game_state(json_string: str) -> None:
    """
    Updates the game state for the currently logged-in user in the database.
    If the user does not exist in the database, an error is raised.
    Parameters:
        json_string (str): JSON string containing game state data.
    """
    try:
        current_user = session_manager.get_current_user()

        if not current_user:
            print("Error: No user is currently logged in.")
            return

        # Parse the JSON string
        game_state_data = json.loads(json_string)

        con = _connect()
        cur = con.cursor()

        cur.execute("SELECT 1 FROM users WHERE username = ?", (current_user,))
        user_exists = cur.fetchone()

        if not user_exists:
            raise ValueError(f"Error: User '{current_user}' does not exist in the database.")

        cur.execute("""
            UPDATE users 
            SET game_state = ? 
            WHERE username = ?
        """, (json.dumps(game_state_data), current_user))

        con.commit()
        con.close()
        print(f"Game state successfully updated for user: {current_user}")

    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
    except sqlite3.DatabaseError as e:
        print(f"Database error: {e}")
    except ValueError as e:
        print(e)  # Custom error when the user does not exist
    except Exception as e:
        print(f"Unexpected error storing game state: {e}")

def get_game_state() -> dict:
    """
    Retrieves the game state from the database for the currently logged-in user.
    Returns:
        dict or None: The game state as a dictionary if found, otherwise None.
    """
    try:
        current_user = session_manager.get_current_user()

        if not current_user:
            print("Error: No user is currently logged in.")
            return None

        con = _connect()
        cur = con.cursor()

        cur.execute("SELECT game_state FROM users WHERE username = ?", (current_user,))
        row = cur.fetchone()

        con.close()

        # If a game state exists
        if row and row[0]:  
            # Convert JSON string back to a Python dictionary
            return json.loads(row[0])  
        else:
            print(f"No game state found for user: {current_user}")
            return None

    except Exception as e:
        print(f"Error retrieving game state: {e}")
        return None
