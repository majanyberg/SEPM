import json
from WordSearch.model.category import Category

class Backend:

    def get_words(category: Category, placeholder, placeholder2):
        """
        Reads a JSON file and fetches words for the given category.

        :param category: The category to fetch words for.
        :return: A dictionary with 'swedish', 'english', and 'hints' lists.
        """
        json_file = "words.json"  # Path to the JSON file
        try:
            with open(json_file, "r", encoding="utf-8") as file:
                data = json.load(file)  # Load JSON data
                return data.get(category.value, {"swedish": [], "english": [], "hints": []})  # Fetch words for category
        except FileNotFoundError:
            print(f"Error: File '{json_file}' not found.")
            return {"swedish": [], "english": [], "hints": []}
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON format in '{json_file}'.")
            return {"swedish": [], "english": [], "hints": []}