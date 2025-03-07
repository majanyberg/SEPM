class WordTracker:
    def __init__(self, word_dict):
        """
        Initializes the WordTracker with a dictionary of words and their coordinates.
        """
        self.word_dict = word_dict  # Dictionary storing words and their coordinates
        self.current_word = None  # The word being currently tracked
        self.last_coord = None  # Last checked coordinate

    def check_coordinate(self, coord):
        """
        Checks if a coordinate is part of a word and follows the sequential order.

        Returns:
            1 - If the coordinate is the first letter of a word.
            1 - If it's in the middle of the word and follows the last coordinate.
            2 - If it's the last letter of a word and follows the sequence.
            0 - If it's not in any word or is not following the correct sequence.
        """
        # Check if the coordinate is the FIRST letter of any word
        for word, coords in self.word_dict.items():
            if coord == coords[0]:  # If it's the starting letter
                self.current_word = word
                self.last_coord = coord
                return 1  # Valid start

        # If we already started a word, check continuation
        if self.current_word:
            coords = self.word_dict[self.current_word]

            if coord in coords:
                index = coords.index(coord)

                # Ensure it's directly connected to the last coordinate
                if self.last_coord is not None:
                    last_index = coords.index(self.last_coord)

                    if index == last_index + 1:  # Must be the next letter
                        self.last_coord = coord
                        return 2 if index == len(coords) - 1 else 1  # Last letter = 2, otherwise 1

        return 0  # Not part of a word or incorrect sequence
