class CharacterController:
    """
    A controller to manage characters, including creation, retrieval, updating, and deletion.

    Attributes:
        character_list (list): Static list to store all characters inside the class.
        id (int): A static ID counter for unique character identification.
    """

    character_list = []
    id = 0  # Static variable

    def create_character(self, name_of_file, clothes):
        """
        Creates a new character and adds it to the character list.
        The clothes are expected to be in this format:
        [[type,color,texture,center_position,word_position],...]

        This is a list of list if there are multiple characters.
        But it can also be just a normal list with each parameter:
        [type,color,texture,center_position,word_position]

        The created character will be added to the character list and the database, as well as being returned.

        Args:
            name_of_file (str): The name of the file to get characters image from.
            clothes (list): A list of the clothes associated with the character.

        Returns:
            Character: A character object.
        """
        pass

    def verify_user_input(self, character_id, user_input):
        """
        Verifies if the user input is correct.

        Args:
            user_input (any): The input to be verified.
            character_id (int): The ID of the character.

        Returns:
            bool: True if the input is a valid string, False otherwise.

        Raises:
            TypeError: If the input is not a string.
        """
        pass

    def ask_character(self, character_amount):
        """
        Return character_amount random characters taken from the character_list.

        Args:
            character_amount (int): Number of characters needed.

        Returns:
            list: A list of characters.
        """
        pass

    def fetch_characters_from_database(self, database):
        """
        Get all characters from the database and put them in the character list.

        Args:
            database (any): The database to fetch characters from.

        Returns:
            nothing
        """
        pass

    def remove_character(self, character_id):
        """
        Removes a character from the list and the database, based on their ID.

        Args:
            character_id (int): The ID of the character to remove.

        Returns:
            bool: True if the character was removed, False if not found.
        """
        pass

    def update_character(self, character_id, attribute_to_change, new_value, clothe_position=0):
        """
        Update whatever attribute needs to be changed.
        List of accepted attributes:
        path_to_file, clothes, word_position, center_position

        If clothes or any position is given in argument, you have to specify the clothe's position in parameters.
        For Position give a Tuple type object: (x,y)
        The standard clothe's position is from top to bottom.
        For example, if the character has a hat a t-shirt and a pant:
        0 = hat, 1 = t-shirt, 2 = pant
        Without a hat:
        0 = t-shirt, 1 = pant

        If two clothes are at the same height, use alphabetical order priority.

        If clothes argument is given, you will have to rewrite the whole clothe this (not every clothes) way:
        [type,color,texture,center_position,word_position]

        Args:
            character_id (int): The ID of the character to update.
            attribute_to_change (str): The name of the attribute to update.
            new_value (any): The new value of the character.
            clothe_position: Position of the clothe in the list.

        Returns:
            bool: True if the update was successful, False otherwise.
        """
        if character_id not in self.character_list: return False
        elif attribute_to_change == 'path_to_file':
            self.character_list[character_id].path_to_file = new_value
            return True
        elif attribute_to_change == 'clothes':
            if not isinstance(new_value, list): return False
            self.character_list[character_id].clothes[clothe_position] = new_value
            return True
        elif attribute_to_change == 'word_position':
            if not isinstance(new_value, tuple): return False
            self.character_list[character_id].clothes[clothe_position].edit_word_center(new_value)
            return True
        elif attribute_to_change == 'center_position':
            if not isinstance(new_value, tuple): return False
            self.character_list[character_id].clothes[clothe_position].edit_center_center(new_value)
            return True
        else: return False

    def retrieve_nouns(self, character_id_list):
        """
        Retrieves 15 nouns from the database,
        excluding the nouns contained in the character_id_list given in parameter.

        Args:
            character_id_list (list): List of characters's ID.

        Returns:
            list: A list of 15 nouns.
        """
        pass

    def retrieve_adjectives(self, character_id_list):
        """
        Retrieves 20 adjectives from the database,
        excluding the adjectives contained in the character_id_list given in parameter.

        Args:
            character_id_list (list): List of characters's ID.

        Returns:
            list: A list of 20 adjectives.
        """
        pass
