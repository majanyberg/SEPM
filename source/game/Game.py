from Score import Score
from GameState import GameState


class Game:
    def __init__(self):
        """
        Initialize the game with default values for lives, score, difficulty, and game state.
        """
        self.lives = 3
        self.difficulty = "Easy"
        self.questions = []
        self.active = False
        self.score = Score()
        self.game_state = GameState()

    def start_new_game(self):
        """
        Start a new game session, resetting lives, score, and game state.
        If a game session is already active, restart the game instead.
        """
        if self.active:
            print("Game session already active. Restart instead.")
            return

        print("Initializing new game session...")
        self.lives = 3
        self.score.reset()
        self.game_state = GameState()
        self.questions = self.fetch_questions()
        self.active = True

    def fetch_questions(self):
        """
        Fetch the questions from the backend.
        """
        print("Fetching questions from backend...")
        try:
            questions = ["What time is it?", "How do you say 12:30 in Swedish?"]
            return questions
        except Exception:
            print("Error fetching questions. Retrying...")
            return []

    def reset_game(self):
        """
        Reset the game session by restarting the game if there is an active session.
        """
        if not self.active:
            print("No active game session to reset.")
            return

        print("Resetting game session...")
        self.start_new_game()
      
