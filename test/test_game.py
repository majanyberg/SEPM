import unittest
from unittest.mock import MagicMock
from source.game.Game import Game

class TestGame(unittest.TestCase):

    def setUp(self):
        """Initialize a new game instance before each test"""
        self.game = Game()
        self.game.fetch_questions = MagicMock(return_value=["Mock Question 1", "Mock Question 2"])

    def test_initial_state(self):
        """Test if the game initializes with correct default values"""
        self.assertEqual(self.game.lives, 3)
        self.assertFalse(self.game.active)

    def test_start_game(self):
        """Test if new game starts correctly"""
        self.game.start_new_game()
        self.assertEqual(self.game.lives, 3)
        self.assertTrue(self.game.active)

    def test_game_over(self):
        """Test if game ends when lives reach zero"""
        self.game.start_new_game()
        self.game.lives = 1
        self.game.answer_question("wrong", "correct")
        self.assertFalse(self.game.active)

    def test_reset_game(self):
        """Test if the game resets properly"""
        self.game.start_new_game()
        self.game.answer_question("wrong", "correct")
        self.game.reset_game()
        self.assertEqual(self.game.lives, 3)
        self.assertTrue(self.game.active)

if __name__ == '__main__':
    unittest.main()
