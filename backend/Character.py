from backend.ClothingItem import ClothingItem
class Character:
    """
    Represents a character with an ID, a list of clothes, and a file path.
    """

    def __init__(self, id, clothes, path_to_file):
        """
        Initializes a Character object.

        Args:
            id (int): The unique identifier of the character.
            clothes (list): A list of Clothe objects associated with the character.
            path_to_file (str): The file path related to the character.
        """
        self.id = id
        self.clothes = clothes
        self.path_to_file = path_to_file

    def getID(self):
        return self.id
    
    def getClothes(self):
        return self.clothes
    
    def getPath(self):
        return self.path_to_file