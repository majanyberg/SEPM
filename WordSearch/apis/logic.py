from model.player import Player
from model.category import Category
from model.grid import Grid
from model.word_list import WordList
import random
from model.wordtracker import WordTracker

class Logic:
    def __init__(self):
        """
        Initializes a new Logic object to handle the game logic.
        The player is set to None initially.
        """
        self.player: Player | None = None  # player is currently None

    def init_player(self, health_points: int, hint_count: int, category: Category) -> bool:
        """
        Creates a new player with the given attributes and initializes the game state.

        Args:
            health_points (int): The initial health points of the player.
            hint_count (int): The number of hints available to the player.
            category (Category): The selected category for the game.

        Returns:
            bool: Returns `True` if the player was successfully created and initialized, `False` otherwise.
        """
        
        word_list = WordList()
        word_list.fetch_data(category)
        self.sw_words, self.en_words, self.hints = word_list.get_lists() # retrieving words
        self.player = Player(health_points, hint_count, category)
        self.correct_matches = 0
        self.word_pairs = len(self.sw_words)
        print(self.word_pairs)
        self.__set_grid(self.sw_words, self.en_words)  # initialize grid
        self.coords = self.player.get_coords()
        print(self.coords)
        self.word_tracker = WordTracker(self.coords)
        return True  # success

    def __set_grid(self, sv_words, en_words):
        """
        Initializes and generates the game grid based on the given list of words.

        Args:
            words (list of str): A list of words to populate the grid with.
        """
        grid = Grid(20, sv_words, en_words)  # 20x20 grid with words
        grid.generate()  # generate grid
        self.player.set_grid(grid.getGrid())  # set player grid

    def new_move(self, sv_word: str, en_word: str) -> Player:
        """
        Processes a new move by checking the word match via the GRID object.
        A faulty move reduces the player's health points.

        Args:
            sv_word (str): The word in the source language (Swedish).
            en_word (str): The word in the target language (English).

        Returns:
            Treu if the move is correct, otherwise false.
        
        Raises:
            ValueError if the english word has been correctly guessed before.
        """
        if self.player.check(sv_word, en_word) == True:
            self.correct_matches += 1
            return True
        else:
            self.player.reduce_hp()
            return False

    def game_over(self):
        print('Game over')

    def get_hp(self):
        """
        Retrieves the player's current health points.

        Returns:
            int: The player's current health points.

        Raises:
            ValueError: If no player has been initialized yet.
        """
        if self.player is not None:
            return self.player.get_hp()
        raise ValueError("No player has been initialized")

    def get_grid(self):
        """
        Retrieves the player's current grid.

        Returns:
            list: The current grid associated with the player.

        Raises:
            ValueError: If no player has been initialized yet.
        """
        if self.player is not None:
            return self.player.get_grid_mat()
        raise ValueError("No player has been initialized")

    def get_hints_left(self):
        """
        Retrieves the number of hints the player has left.

        Returns:
            int: The number of hints left for the player.

        Raises:
            ValueError: If no player has been initialized yet.
        """
        if self.player is not None:
            return self.player.get_hints_left()
        raise ValueError("No player has been initialized")

    def get_hint(self):
        """
        Provides a hint from the list of available hints if the player has any left.
        Reduces the hint count by one if a hint is provided.

        Returns:
            tuple: 
                - bool: `True` if a hint was provided, `False` if no hints are left.
                - list: A list containing the hint or an empty list if no hints are left.
        """
        if self.player is not None:
            if self.player.get_hints_left() > 0:
                self.player.reduce_hints()
                return True, random.choice(self.hints)
            else:
                return False, []  # no available hints
        raise ValueError("No player has been initialized")
    
    def player_is_alive(self):
        return (self.player.get_hp() > 0)
    
    def player_won(self):
        return (self.correct_matches == self.word_pairs)
    
    def get_correct_matches(self):
        return self.correct_matches
    """
    def validate(self, x, y):
        for coords in self.coords.values():
            if (x, y) in coords:
                return True
        return False
    """
    def validate(self, x, y):
        """
        Checks if a coordinate is part of a valid word sequence.

        Returns:
            True if valid move, False otherwise.
        """
        if self.word_tracker:
            return self.word_tracker.check_coordinate((x, y))
        return False  # If no WordTracker initialized, return False

        

