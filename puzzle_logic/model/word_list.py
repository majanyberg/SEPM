import sys
sys.path.append("..")
from .category import Category
from puzzle_logic.apis import backend_API

#backend module
#import backend_API


class WordList:
    def __init__(self):
        """
        Initializes a Word List instance.
        """
        self.swedish = []
        self.english = []
        # hints contains list of hints, each word has three hints.
        self.hints = []
    
    def fetch_data(self, category: Category):
        # Default settings: difficulty = "easy", count: 20.
        print(f'category = {category.value}')
        data = backend_API.get_words(category.value, 'EASY', 20)
        print(f'data={data}')
        
        for word in data:
            swedish = word["swedish"]
            english = word["english"]
            hints = word["hints"]

            self.swedish.append(swedish)
            self.english.append(english)
            self.hints.append(hints)

    """

    """
    def get_lists(self):
        print(f'get_lists return hints: {self.hints}, sv_words_ {self.swedish}')
        "Returns the three lists"
        return self.swedish, self.english, self.hints

    def get_list_of_lists(self):
        "If we want to return a single list containing the three lists."
        return [self.swedish, self.english, self.hints]