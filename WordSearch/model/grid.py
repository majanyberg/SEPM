import random
import string

class Grid:

    def __init__(self, size, sv_words, en_words):
        """
        Initializes the word search grid with a given size and words list.

        Args:
            size (int): Size of the grid
            words (list): List with the words to be search
        """
        self.size = size
        self.sv_words = [word.upper() for word in sv_words]
        self.en_words = [word.upper() for word in en_words]
        self.word_map = dict(zip(sv_words, en_words))
        self.guessed_english = set()  # To track guessed English words
        self.word_positions = {}
        print(f'map={self.word_map}')
        self.grid = [[' '] * size for _ in range(size)]
        self.directions = [
            (0, 1),   # Right
            (0, -1),  # Left
            (-1, 0),  # Up
            (1, 0),   # Down
            (1, 1),   # Down-right
            (1, -1),  # Down-left
            (-1, 1),  # Up-right
            (-1, -1)  # Up-left
        ]


    def can_place_word(self, word, row, col, direction):
        """
        Checks if a word can be placed at a given position with a given direction.

        Args:
            word (str): The word to place
            row (int): The starting row
            col (int): The starting column
            direction (tuple): The row and column direction
        
        Returns:
            True if the word can be placed, False otherwise
        """
        for i in range(len(word)):
            r = row + i * direction[0]
            c = col + i * direction[1]
        
            # Check if the word can fit in the grid
            if r < 0 or r >= self.size or c < 0 or c >= self.size:
                return False
            
            # Check if the word can be placed in the grid
            if self.grid[r][c] != ' ' and self.grid[r][c] != word[i]:
                return False
        
        return True
    

    def place_word(self, word):
        """
        Places a word randomly in the grid, after checking that it can be placed.
    
        Args:
            word (str): The word to place
        """
        placed = False
        while not placed:
            # Randomly choose a starting position and direction
            direction = random.choice(self.directions)
            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)

            # Check if the word can be placed in the grid
            can_place = self.can_place_word(word, row, col, direction)

            # Place the word in the grid
            if can_place:
                self.word_positions[word] = []
                for i in range(len(word)):
                    r = row + i * direction[0]
                    c = col + i * direction[1]
                    self.grid[r][c] = word[i]
                    self.word_positions[word].append((r,c))
                placed = True
    
    def get_coords(self):
        return self.word_positions

    def fill_empty_spaces(self):
        """
        Fills empty spaces in the grid with random letters.
        """
        for r in range(self.size):
            for c in range(self.size):
                if self.grid[r][c] == ' ':
                    self.grid[r][c] = random.choice(string.ascii_uppercase)

    
    def check(self, sv_word, en_word):
        """
        Checks if the given sv_word correctly matches the en_word.
        If they match, remove the pair from self.word_map.
        Ensures that an English word cannot be guessed twice.

        :param sv_word: Word from the first language (Swedish).
        :param en_word: Word from the second language (English).
        :return: True if they match (and are removed), raises exception if en_word already guessed.
        """
        # Ensure English word hasn't been guessed yet
        if en_word in self.guessed_english:
            raise ValueError(f"The English word '{en_word}' has already been correctly guessed.")

        if sv_word in self.word_map:
            if self.word_map[sv_word] == en_word:
                del self.word_map[sv_word]  # Remove the matched pair
                self.guessed_english.add(en_word)  # Mark the English word as correctly guessed
                return True
            else:
                return False  # Incorrect match


    def generate(self):
        """
        Generates the word search grid by placing words 
        and filling empty spaces with random letters.
        """
        for word in self.sv_words:
            self.place_word(word)
        self.fill_empty_spaces()


    def getGridMat(self):
        """
        Returns the grid as a list of lists (list of all rows).
        """
        return self.grid
    

    def getGrid(self):
        return self