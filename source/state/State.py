from source.state.Score import Score

class GameState:
    """Component that keeps track of the gamestate"""

    def __init__(self, level: int = 1, max_score: int = 0):
        if not self.is_valid_level(level):
            raise ValueError("Invalid level: must be between 1 and 3.")
        
        # Initialize variables to be used to determine stats and 
        self.level = level
        self._questions_answered = 0
        self._correct_in_row = 0
        self._questions_answered_correctly = 0
        self.score = Score(max_score)
    
    def correct_answer(self) -> None:
        """
        Used when an user has answred the question correctly.
        This keeps track of the state of the game i.e. data used for scoring,
        but also used to incrememnt (or decrement) the level.
        """
        self._questions_answered += 1
        self._questions_answered_correctly += 1
        self._correct_in_row += 1
        self.score.add_points(10)

    def wrong_answer(self) -> None:
        """Used when an user has answred the question incorrectly.
        """
        self._correct_in_row = 0 # reset 
        self._questions_answered += 1
        self.score.subtract_points(5)

    # Getters to be able to change the datastructure to fit better
    # with other components.
    def get_amount_correct(self) -> int:
        return self._questions_answered_correctly
    
    def get_row_correct(self) -> int:
        return self._correct_in_row

    def get_level(self) -> int:
        return self.level
    
    def is_valid_level(self, level: int) -> bool:
        return 1 <= level <= 3