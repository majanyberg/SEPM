import sqlite3

# Internal functions
def _connect():
    """
    Establishes a connection to the SQLite database.
    
    Returns:
        sqlite3.Connection or None: Database connection if successful, otherwise None.
    """
    try:
        conn = sqlite3.connect("backend.db")
        return conn
    except Exception as e:
        print(f"Unexpected error while connecting to the database: {e}")
        return None

def _get_table_columns(table_name: str) -> set:
    """
    Retrieves column names of a given table.
    Args:
        table_name (str): The name of the table.
    Returns:
        set: A set of column names in the table, or an empty set if the table does not exist.
    """
    try:
        conn = _connect()
        cur = conn.cursor()
        cur.execute(f"PRAGMA table_info({table_name})")
        columns = {row[1] for row in cur.fetchall()}
        conn.close()
        return columns

    except sqlite3.OperationalError as e:
        print(f"Error: Table '{table_name}' does not exist or cannot be accessed. Details: {e}")
        return set()
    except sqlite3.DatabaseError as e:
        print(f"Database error: {e}")
        return set()
    except Exception as e:
        print(f"Unexpected error: {e}")
        return set()
