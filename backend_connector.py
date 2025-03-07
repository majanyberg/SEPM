""" Required Functions from Backend Module
Function	                Purpose
load_progress() -> dict	    Loads saved game progress.
save_progress()	            Saves current game progress.
reset_progress()	        Resets all saved progress.
get_leaderboard() -> list	Returns the leaderboard of top scores."""

import json
import os

SAVE_FILE = "assets/progress.json"

class BackendConnector:
    def __init__(self):
        """Handles saving/loading game progress and leaderboard management."""
        self.file_path = SAVE_FILE
        self.data = self.load_progress()

    def load_progress(self):
        """Load saved game progress from the backend."""
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as f:
                return json.load(f)
        return {"scores": {}, "leaderboard": []}

    def save_progress(self):
        """Save current game progress to the backend."""
        with open(self.file_path, 'w') as f:
            json.dump(self.data, f)

    def reset_progress(self):
        """Reset game progress."""
        self.data = {"scores": {}, "leaderboard": []}
        self.save_progress()

    def get_leaderboard(self):
        """Retrieve the leaderboard."""
        return sorted(self.data.get('leaderboard', []), reverse=True)[:5]
