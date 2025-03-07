import Position
class Clothe:
    """
    Represents a piece of clothing with various attributes, including type, color, texture,
    and positioning information.
    """

    def __init__(self, type, color, texture, center_position: Position, word_position: Position):
        """
        Initializes a Clothe object.

        Args:
            type (str): The type of clothing (e.g., shirt, pants).
            color (str): The color of the clothing.
            texture (str): The texture of the clothing (e.g., smooth, rough).
            center_position (position): The (x, y) coordinates of the center position.
            word_position (position): The (x, y) coordinates of the word position.
        """
        self.type = type
        self.color = color
        self.texture = texture
        self.center_position = center_position
        self.word_position = word_position

    def edit_clothe_center(self, values: tuple):
        """
        Edits the center position of the clothing.

        Args:
            values (tuple): The new center position of the clothing.
        """
        self.center_position.changePosition(values[0], values[1])

    def edit_word_center(self, values: tuple):
        """
        Edits the center position of the word attached to the clothing.

        Args:
            values (tuple): The new center position of the word.
        """
        self.word_position.changePosition(values[0], values[1])