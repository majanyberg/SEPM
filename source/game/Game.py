from source.state.State import GameState
from source.level.Level import UserLevelManager
from source.fetchQA.FetchQA import fetch_qa_temp, fetch_questions_from_backend

class Game:
    def __init__(self):
        """
        Initialize the game with default values for lives, score, and game state.
        """
        self.lives = 3
        self.questions = []
        self.active = False
        self.game_state = GameState()
        self.level_manager = UserLevelManager(initial_level=self.game_state.get_level())

    def start_new_game(self):
        """
        Start a new game session, resetting lives, score, and game state.
        If a game session is already active, restart the game instead.
        """
        
        if self.active:
            print("Game session already active. Restarting instead.")
            # return: we would be running a dead return on test.test_game.TestGame.test_reset_game
        

        print("Initializing new game session...")
        self.lives = 3
        self.game_state = GameState()
        self.questions = self.fetch_questions()
        self.active = True
        print("New game started.")

    def fetch_questions(self):
        """Fetch questions from the backend or fallback to local JSON if unavailable."""
        level = self.game_state.get_level()
        print(f"Fetching questions for level {level}...")
        try:
        #     questions = fetch_qa_temp(self.game_state.level)
        #     return questions
        # except Exception:
        #     print("Error fetching questions. Retrying...")
        #     return []
            questions = fetch_questions_from_backend(level)
            if not questions:
                print("Backend unavailable, loading from local JSON...")
                questions = fetch_qa_temp(level)

            return questions if questions else ["No available questions."]
        except Exception as e:
            print(f"Error fetching questions: {e}")
            return ["Error loading questions."]
        
    def answer_question(self, user_answer, correct_answer):
        """Process the user's answer, update score and game state, and check for game over."""
        if not self.active:
            print("Game is not running. Start a new game first.")
            return
        
        if user_answer.strip().lower() == correct_answer.strip().lower():
            print("Correct answer!")
            self.game_state.correct_answer()
        else:
            print("Wrong answer.")
            self.game_state.wrong_answer()
            self.lives -= 1
            print(f"Remaining lives: {self.lives}")

        new_level = self.level_manager.update_level(self.game_state.score.get_score())
        self.game_state.level = new_level

        if self.lives <= 0:
            self.end_game()

    def end_game(self):
        """End the game session, display the final score, and reset the state."""
        print("Game over!")
        print(f"Final score: {self.game_state.score.get_score()}")
        self.active = False
        self.game_state = GameState()
        print("Game session ended.")

    def reset_game(self):
        """
        Reset the game session by restarting the game if there is an active session.
        """
        if not self.active:
            print("No active game session to reset.")
            return

        print("Resetting game session...")
        self.start_new_game()
      
