import unittest
from source.state.State import GameState

class TestSetup(unittest.TestCase):
    def test_game_state_init(self):
        gs = GameState()

        # No questions shall be correct as the gamestate is fresh.
        self.assertEqual(gs._questions_answered, 0)

        # No questions in row shall be answered as the gamestate is fresh.
        self.assertEqual(gs._correct_in_row, 0)

        # Level shall be 1 as default.
        self.assertEqual(gs.level, 1)
        self.assertEqual(gs.get_level(), 1)

    def test_different_values_init(self):
        # Positive test cases
        gs2 = GameState(2)
        gs3 = GameState(3)
        gs4 = GameState(4)

        # Negative test cases
        with self.assertRaises(ValueError):
            GameState(-1)
            GameState(6)


class TestAnswering(unittest.TestCase):
    def test_get_one_question_correct(self):
        gs = GameState() # gs has 0 correct answers.

        for _ in range(10):
            print(gs.get_amount_correct())
            gs.correct_answer() # perform 10 correct answers

        self.assertEqual(gs.get_row_correct(), 10)
        self.assertEqual(gs.get_amount_correct(), 10)

        gs.wrong_answer()

        self.assertEqual(gs.get_row_correct(), 0)
        self.assertEqual(gs.get_amount_correct(), 10)


class TestUtils(unittest.TestCase):
    def test_is_valid_level(self):
        gs = GameState()
        for i in range(1, 5):
            self.assertTrue(gs.is_valid_level(i), 
                "Does not approve valid levels.")

        for i in range(6, 10):
            self.assertFalse(gs.is_valid_level(i),
                "Does approve non-valid levels.")

if __name__ == '__main__':
    unittest.main()