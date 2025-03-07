from __future__ import annotations
from .category import Category
from .grid import Grid

class Player:
    def __init__(self, hp: int, hints_left: int, category: Category):
        """
        Initializes a Player instance.

        Args:
            hp (int): The player's health points.
            hints_left (int): The number of hints available to the player.
            category (Category): The category from which to fetch words for the game.

        Returns:
            None: The constructor does not return a value.
        """
        self.hp = hp
        self.hints_left = hints_left
        self.category = category
        self.grid = None

    def set_grid(self, grid : Grid) -> None:
        """
        Sets the grid for the player.

        Args:
            grid: The grid object associated with the player.

        Returns:
            None
        """
        self.grid = grid
    
    def get_category(self) -> Category:
        """
        Retrieves the category associated with the player.

        Returns:
            Category: Current Category.
        """
        return self.category
        

    def get_hp(self) -> int:
        """
        Gets the current HP (health points) of the player.

        Returns:
            int: The player's current health points.
        """
        return self.hp
        
    
    def get_grid_mat(self):
        """
        Retrieves the grid associated with the player.

        Returns:
            Grid: The grid associated with the player.

        Raises:
            ValueError: If the grid has not been initialized yet.
        """
        if self.grid is not None:
            return self.grid.getGridMat()
        else:
            raise ValueError("No Grid has been initialized")

    def reduce_hints(self) -> None:
        """
        Reduces the player's available hints by 1.

        Returns:
            None: This method does not return a value.
        """
        self.hints_left -= 1
    
    
    def get_hints_left(self) -> int:
        """
        Gets the number of hints left for the player.

        Returns:
            int: The number of hints the player has left.
        """
        return self.hints_left
    
    def reduce_hp(self) -> None:
        """
        Reduces the player's health points by 1.

        Returns:
            bool: True if the player is still alive, False otherwise
        """
        self.hp -= 1
        return self.hp > 0
    
    def get_coords(self):
        if self.grid is not None:
            return self.grid.get_coords()
        else:
            raise ValueError("No Grid has been initialized")
        
    
    def check(self, sv_word : str, en_word : str):
        """
        Checks if the two words are matching and is in scope

        Args:
            sv_word (str): The word in the source language to check
            en_word (str): The word in the target language to check
        
        Returns:
            bool: True if the words match. False otherwise
        """
        return self.grid.check(sv_word, en_word)
