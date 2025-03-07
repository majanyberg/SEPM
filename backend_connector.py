import json

from backend.backend_API import (
    get_game_state,
    store_game_state,
    get_user,
    get_times,
    create_user,
    delete_user,
    session_manager,
    update_cur_user,
    get_cur_user_stats,
    increase_words_learned,
    get_words_learned
)

class BackendConnector:
    """
    Handles saving/loading game progress, leaderboard management, and basic user operations
    by interfacing with the backend API via the sessionmanager module.
    """

    def __init__(self):
        self.data = self.load_progress()
        self.session = session_manager
    
    def fetch_questions(self, difficulty: str = "EASY") -> list:
        """Fetch questions from the backend API."""
        try:
            return get_times(difficulty)
        except Exception as e:
            print(f"Error fetching questions: {e}")
            return []

    def load_progress(self):
        """Load saved game progress from the backend using the API."""
        try:
            progress = get_game_state()
            if progress:
                return progress
        except Exception as e:
            print(f"Error loading game state from backend: {e}")
        return {"scores": {}, "leaderboard": []}

    def save_progress(self):
        """Save the current game progress to the backend using the API."""
        try:
            store_game_state(json.dumps(self.data))
        except Exception as e:
            print(f"Error saving game state to backend: {e}")

    def reset_progress(self):
        """Reset game progress using the backend API."""
        self.data = {"scores": {}, "leaderboard": []}
        self.save_progress()

    def get_leaderboard(self):
        """Retrieve the leaderboard from the current game state."""
        leaderboard = self.data.get('leaderboard', [])
        return sorted(leaderboard, reverse=True)[:5]


    # User Management Functions
    def get_user_info(self, username: str) -> dict:
        """Retrieve user information for the given username."""
        try:
            return get_user(username)
        except Exception as e:
            print(f"Error retrieving user info for {username}: {e}")
            return {}

    def create_new_user(self, username: str, real_name: str = None, age: int = 0,
                        country: str = None, user_type: str = None, total_time: int = 0, 
                        words_learned: int = 0) -> None:
        """Create a new user in the backend."""
        try:
            create_user(username, real_name, age, country, user_type, total_time, words_learned)
        except Exception as e:
            print(f"Error creating new user {username}: {e}")

    def delete_user_account(self, username: str) -> None:
        """Delete a user from the backend."""
        try:
            delete_user(username)
        except Exception as e:
            print(f"Error deleting user {username}: {e}")

    # Session Management Functions
    def login_user(self, username: str) -> str:
        """Log in the user and return the session token."""
        try:
            return self.session.login(username)
        except Exception as e:
            print(f"Error logging in user {username}: {e}")
            return ""

    def logout_user(self) -> None:
        """Log out the current user."""
        try:
            self.session.logout()
        except Exception as e:
            print(f"Error logging out: {e}")

    def update_current_user(self, column: str, value) -> None:
        """Update a field in the current user's profile."""
        try:
            update_cur_user(column, value)
        except Exception as e:
            print(f"Error updating current user: {e}")

    def get_current_user_stats(self) -> dict:
        """Retrieve statistics for the currently logged-in user."""
        try:
            return get_cur_user_stats()
        except Exception as e:
            print(f"Error retrieving current user stats: {e}")
            return {}

    def increase_user_words_learned(self, value: int) -> None:
        """Increase the count of words learned for the current user."""
        try:
            increase_words_learned(value)
        except Exception as e:
            print(f"Error increasing words learned: {e}")

    def get_user_words_learned(self) -> int:
        """Retrieve the number of words learned for the current user."""
        try:
            return get_words_learned()
        except Exception as e:
            print(f"Error getting words learned: {e}")
            return 0