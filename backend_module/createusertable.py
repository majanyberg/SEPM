from backend_module.user_management import _connect, _get_table_columns

def create_users_table():
    try:
        conn = _connect()  # Make sure this connects to the right database
        cur = conn.cursor()

        # Create the users table
        query = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            real_name TEXT,
            age INTEGER,
            country TEXT,
            user_type TEXT,
            total_time INTEGER DEFAULT 0,
            words_learned INTEGER DEFAULT 0
        );
        """
        cur.execute(query)
        conn.commit()
        conn.close()
        print("Users table created successfully.")

    except Exception as e:
        print(f"Unexpected error while creating users table: {e}")

# Call the function once to create the table
create_users_table()