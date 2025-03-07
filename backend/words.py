class Difficulty:
    EASY = 1
    MEDIUM = 2
    HARD = 3
    MIXED = 4

class Category:
    CLOTHING = 1
    FURNITURE = 2
    KITCHEN = 3
    MIXED = 4

def get_words_from_category(category: Category, difficulty: Difficulty, count: int=5):
    """Get a list of Swedish words with their English translation and other related data

    :param category: Category of words. One of Category.CLOTHING, Category.FURNITURE, Category.KITCHEN or Category.MIXED (default)
    :param difficulty: Difficulty of words. One of Difficulty.EASY, Difficulty.MEDIUM, Difficulty.HARD, Difficulty.MIXED (default)
    :param count: Number of words to return
    :return: A list of words along with their English translation and a number of hints about the word. If there is an image associated with the word, its filepath will be returned too.
    Example: [{"swedish": "tröja", "english": "tröja", "hints": ["hint 1", "hint 2", "hint 3"], "image_file": "words/shirt.png"}]
    """
    return [
        {
            "swedish": "tröja",
            "english": "shirt",
            "hints": [
                "First hint",
                "Second hint",
                "Third hint",
            ],
            "image_file": "words/shirt.png"
        },{
            "swedish": "byxor",
            "english": "pants",
            "hints": [
                "First hint",
                "Second hint",
                "Third hint",
            ]
        },{
            "swedish": "strumpor",
            "english": "socks",
            "hints": [
                "First hint",
                "Second hint",
                "Third hint",
            ],
            "image_file": "words/socks.png"
        },{
            "swedish": "handskar",
            "english": "gloves",
            "hints": [
                "First hint",
                "Second hint",
                "Third hint",
            ]
        },{
            "swedish": "jacka",
            "english": "jacket",
            "hints": [
                "First hint",
                "Second hint",
                "Third hint",
            ]
        }
    ]

def get_times(difficulty: Difficulty =Difficulty.MIXED, count: int=5):
    """Get a list of times along with their Swedish names

    :param difficulty: Difficulty of times. Should be one of Difficulty.EASY, Difficulty.MEDIUM, Difficulty.HARD or Difficulty.MIXED (default)
    :param count: Number of items to return
    :return: A list of times along with their swedish names. Example: [{"time": "11:00", "swedish": "elva"}, ...]
    """
    return [
        {
            "time": "11:00",
            "swedish": "elva",
            "image_file": "times/1100.png"
        },
        {
            "time": "11:30",
            "swedish": "halv tolv",
            "image_file": "times/1130.png"
        },
        {
            "time": "22:00",
            "swedish": "tio",
            "image_file": "times/2200.png"
        },
        {
            "time": "22:30",
            "swedish": "halv elva",
            "image_file": "times/1030.png"
        },
        {
            "time": "00:00",
            "swedish": "tolv",
            "image_file": "times/0000.png"
        }
    ]