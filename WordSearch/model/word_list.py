import sys
sys.path.append("..")
from WordSearch.model.category import Category
from WordSearch.apis.mocked_backend import Backend as backend_API
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
    
    def fetch_data(self, category : Category):
        data = backend_API.get_words(category, None, None)  # Fetch words

        print("DEBUG: Data received from Backend:", data)  # Debugging

        # Ensure we're working with lists
        self.swedish = data.get("swedish", [])
        self.english = data.get("english", [])
        self.hints = data.get("hints", [])

        # Combine words into a list of dictionaries
        word_list = []
        for sw, en, hints in zip(self.swedish, self.english, self.hints):
            word_list.append({"swedish": sw, "english": en, "hints": hints})

        print("DEBUG: Processed word list:", word_list)  # Debugging
        return word_list

    """
    def fetch_data(self, category: Category):

        Fetches data from backend

        Args:
            category: The category from which to fetch words.

        # Default settings: difficulty = "easy", count: 20.
        data = backend_API.get_words(category, "easy", 20)
        
        for word in data:
            swedish = word["swedish"]
            english = word["english"]
            hints = word["hints"]

            self.swedish.append(swedish)
            self.english.append(english)
            self.hints.append(hints)
    """
    def get_lists(self):
        print(f'get_lists return hints: {self.hints}, sv_words_ {self.swedish}')
        "Returns the three lists"
        return self.swedish, self.english, self.hints

    def get_list_of_lists(self):
        "If we want to return a single list containing the three lists."
        return [self.swedish, self.english, self.hints]