import unittest
from unittest.mock import MagicMock
from source.level.Level import QuestionDatabase, UserLevelManager


class TestQuestionDatabase(unittest.TestCase):
    """Test cases for QuestionDatabase"""

    def setUp(self):
        """Create a mock version of QuestionDatabase to avoid connecting to the real database"""
        self.db = QuestionDatabase(
            host="localhost", user="root", password="password", database="question_db"
        )
        self.db.cursor = MagicMock()

    def test_get_questions_by_level(self):
        """Test the number of questions for different levels"""
        self.db.cursor.fetchone.return_value = [10]  # Assume the database query returns 10 questions
        count = self.db.get_questions_by_level(1)
        self.assertEqual(count, 10)

    def tearDown(self):
        """Close the database connection"""
        self.db.close()


class TestUserLevelManager(unittest.TestCase):
    """Test cases for UserLevelManager"""

    def setUp(self):
        """Initialize the UserLevelManager"""
        self.manager = UserLevelManager(initial_level=2)

    def test_level_up(self):
        """Test the level-up logic"""
        new_level = self.manager.update_level(85)  # Should level up if score is above 80
        self.assertEqual(new_level, 3)

    def test_level_down(self):
        """Test the level-down logic"""
        new_level = self.manager.update_level(40)  # Should level down if score is below 50
        self.assertEqual(new_level, 1)

    def test_level_unchanged(self):
        """Test keeping the current level"""
        new_level = self.manager.update_level(70)  # Should remain the same if score is between 50-80
        self.assertEqual(new_level, 2)


if __name__ == "__main__":
    unittest.main()
