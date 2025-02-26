import mysql.connector


class QuestionDatabase:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()

    def get_questions_by_level(self, level):
        """Fetch the number of questions for a given level.
        
        Assumes the 'questions' table has the following fields:
        - id: unique identifier for the question
        - level: the level of the question (1, 2, 3)
        """
        query = "SELECT COUNT(*) FROM questions WHERE level = %s"
        self.cursor.execute(query, (level,))
        return self.cursor.fetchone()[0]

    def close(self):
        """Close the database connection."""
        self.conn.close()


class UserLevelManager:
    def __init__(self, initial_level=1):
        self.level = initial_level

    def update_level(self, score):
        """Update the user level based on their score.

        - score >= 80: level up
        - score < 50: level down
        - Otherwise, the level remains unchanged.
        """
        if score >= 80 and self.level < 3:
            self.level += 1
        elif score < 50 and self.level > 1:
            self.level -= 1
        return self.level
