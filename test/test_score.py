import unittest
from source.state.Score import Score  # Import the Score class

class TestScore(unittest.TestCase):
    def test_add_points(self):
        """Test adding points to the score."""
        score = Score()
        score.add_points(10)
        self.assertEqual(score.get_score(), 10)

        score.add_points(5)
        self.assertEqual(score.get_score(), 15)

    def test_subtract_points(self):
        """Test subtracting points from the score."""
        score = Score()
        score.add_points(20)
        score.subtract_points(5)
        self.assertEqual(score.get_score(), 15)

        score.subtract_points(10)
        self.assertEqual(score.get_score(), 5)

    def test_reset_score(self):
        """Test resetting the score to zero."""
        score = Score()
        score.add_points(10)
        score.reset()
        self.assertEqual(score.get_score(), 0)

    def test_negative_score(self):
        """Test if score can go negative"""
        score = Score(10)
        score.subtract_points(15)
        self.assertEqual(score.get_score(), 0)

if __name__ == '__main__':
    unittest.main()