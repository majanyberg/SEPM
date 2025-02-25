import contextlib
import sqlite3

@contextlib.contextmanager
def connect():
    conn = sqlite3.connect('backend.db')
    cur = conn.cursor()
    try:
        yield cur
    finally:
        conn.commit()
        conn.close()

def seed_words_with_hints():
    """
    Inserts 60 rows into 'words':
      - 20 items for 'clothing'
      - 20 items for 'furniture'
      - 20 items for 'food'
    Each has swedish, english, category, difficulty, hint1, hint2, hint3.
    """

    words_data = [
        # ================== CLOTHING (20 total) ==================
        # 10 EASY
        ("jacka",       "jacket",               "clothing", "EASY",   "Worn on upper body",    "Has zipper or buttons",   "Protects from cold"),
        ("byxor",       "pants",                "clothing", "EASY",   "Leg coverings",         "Often have pockets",      "Worn daily"),
        ("skor",        "shoes",                "clothing", "EASY",   "Protect your feet",     "Comes in pairs",          "Various styles"),
        ("t-shirt",     "t-shirt",              "clothing", "EASY",   "Short sleeves",         "Casual top",              "Often cotton"),
        ("tröja",       "sweater",              "clothing", "EASY",   "Long-sleeved top",      "Warm garment",            "Knitted or fleece"),
        ("sockor",      "socks",                "clothing", "EASY",   "Feet coverings",        "Often cotton or wool",    "Wear under shoes"),
        ("klänning",    "dress",                "clothing", "EASY",   "One-piece garment",     "Worn by women",           "Varies in length"),
        ("kjol",        "skirt",                "clothing", "EASY",   "Lower body garment",    "Worn by women",           "Can be short or long"),
        ("mössa",       "beanie/cap",           "clothing", "EASY",   "Headwear",              "Keeps you warm",          "Worn in winter"),
        ("vantar",      "mittens",              "clothing", "EASY",   "Hand coverings",        "Thumb is separate",       "Worn in winter"),

        # 5 MEDIUM
        ("handskar",    "gloves",               "clothing", "MEDIUM", "Cover entire hand",     "Separate fingers",         "Worn in cold weather"),
        ("skjorta",     "shirt",                "clothing", "MEDIUM", "Collared top",          "Buttons on front",         "Unisex garment"),
        ("kostym",      "suit",                 "clothing", "MEDIUM", "Formal attire",         "Matching jacket & pants",  "Worn on special occasions"),
        ("hatt",        "hat",                  "clothing", "MEDIUM", "Headwear with a brim",  "Fashion or shade",         "Various styles"),
        ("halsduk",     "scarf",                "clothing", "MEDIUM", "Long fabric strip",      "Worn around neck",         "Keeps you warm"),

        # 5 HARD
        ("kalsonger",   "underpants (men)",     "clothing", "HARD",   "Men’s underwear",       "Worn under pants",         "Daily garment"),
        ("trosor",      "underpants (women)",   "clothing", "HARD",   "Women’s underwear",     "Cotton or lace",           "Daily garment"),
        ("strumpbyxor", "tights/pantyhose",     "clothing", "HARD",   "Sheer or thick",        "Waist to feet",            "Often worn with skirts"),
        ("regnjacka",   "rain jacket",          "clothing", "HARD",   "Waterproof coat",       "Used in wet weather",      "Often has a hood"),
        ("badbyxor",    "swim trunks",          "clothing", "HARD",   "Men’s swimwear",        "Used for swimming",        "Also called swim shorts"),


        # ================== FURNITURE (20 total) ==================
        # 10 EASY
        ("stol",        "chair",                "furniture", "EASY",   "For sitting",           "Has 4 legs",               "Can have a backrest"),
        ("bord",        "table",                "furniture", "EASY",   "Flat surface",          "Used for meals",           "Various sizes"),
        ("säng",        "bed",                  "furniture", "EASY",   "For sleeping",          "Uses a mattress",          "In bedroom"),
        ("soffa",       "sofa/couch",           "furniture", "EASY",   "Seats multiple people", "Living room furniture",    "Has soft cushions"),
        ("fåtölj",      "armchair",             "furniture", "EASY",   "Single seat",           "Comfy backrest",           "Often padded"),
        ("lampa",       "lamp",                 "furniture", "EASY",   "Provides light",        "Electric device",          "Floor or table type"),
        ("gardin",      "curtain",              "furniture", "EASY",   "Hangs on window",       "Blocks or filters light",  "Can be decorative"),
        ("matta",       "rug/carpet",           "furniture", "EASY",   "Covers the floor",      "Softens footsteps",        "Often decorative"),
        ("byrå",        "dresser",              "furniture", "EASY",   "Storage furniture",     "Multiple drawers",         "Used for clothing"),
        ("spegel",      "mirror",               "furniture", "EASY",   "Reflective surface",    "Used for grooming",        "Made of glass"),

        # 5 MEDIUM
        ("skrivbord",   "desk",                 "furniture", "MEDIUM", "Work surface",          "Often has drawers",        "Used for studying"),
        ("bokhylla",    "bookshelf",            "furniture", "MEDIUM", "Holds books",           "Multiple shelves",         "Wood or metal"),
        ("tv-bänk",     "tv stand",             "furniture", "MEDIUM", "Holds a television",    "Sometimes has storage",    "Usually in living room"),
        ("nattduksbord","nightstand",           "furniture", "MEDIUM", "Beside the bed",        "Holds lamp/alarm clock",   "May have drawers"),
        ("pall",        "stool",                "furniture", "MEDIUM", "Seat without back",     "Often wooden",             "Can be tall or short"),

        # 5 HARD
        ("skoställ",    "shoe rack",            "furniture", "HARD",   "Organizes shoes",       "Placed near entryway",     "Multiple tiers"),
        ("sideboard",   "sideboard",            "furniture", "HARD",   "Dining room storage",   "Holds plates/dishes",      "Often waist-high"),
        ("klädhängare", "coat rack",            "furniture", "HARD",   "Hangs coats",           "Freestanding or wall",     "In hallway"),
        ("kista",       "chest/trunk",          "furniture", "HARD",   "Storage box",           "Lid on top",               "Traditional or decorative"),
        ("vitrin",      "display cabinet",      "furniture", "HARD",   "Glass doors",           "Shows fine dishes",        "Typically in dining area"),


        # ================== FOOD (20 total) ==================
        # 10 EASY
        ("äpple",       "apple",               "food", "EASY",   "Fruit",              "Red or green",             "Grows on trees"),
        ("mjölk",       "milk",                "food", "EASY",   "Dairy product",      "White color",              "From cows"),
        ("smör",        "butter",              "food", "EASY",   "Made from cream",    "Spread on bread",          "Yellowish color"),
        ("ost",         "cheese",              "food", "EASY",   "Dairy product",      "Many varieties",           "Can be sliced"),
        ("bröd",        "bread",               "food", "EASY",   "Baked dough",        "Basic staple",             "Sliced or loaf"),
        ("potatis",     "potato",              "food", "EASY",   "Root vegetable",     "Starchy",                  "Common in Sweden"),
        ("banan",       "banana",              "food", "EASY",   "Tropical fruit",     "Yellow peel",              "Rich in potassium"),
        ("tomat",       "tomato",              "food", "EASY",   "Red fruit",          "Used in salads",           "Botanically a fruit"),
        ("gurka",       "cucumber",            "food", "EASY",   "Green vegetable",    "High water content",       "Salad ingredient"),
        ("morot",       "carrot",              "food", "EASY",   "Orange root veg",    "High in beta-carotene",    "Often eaten raw"),

        # 5 MEDIUM
        ("kanelbulle",  "cinnamon bun",        "food", "MEDIUM", "Swedish pastry",     "Cinnamon flavor",          "Coffee accompaniment"),
        ("köttbullar",  "meatballs",           "food", "MEDIUM", "Swedish dish",       "Often with lingonberries", "Minced meat mixture"),
        ("lax",         "salmon",              "food", "MEDIUM", "Fish",               "Pink/orange flesh",        "High in omega-3"),
        ("kyckling",    "chicken",             "food", "MEDIUM", "Poultry",            "White meat",               "Widely consumed"),
        ("lingonsylt",  "lingonberry jam",     "food", "MEDIUM", "Tart jam",           "Served with meat",         "Made from red berries"),

        # 5 HARD
        ("blodpudding","blood pudding",        "food", "HARD",   "Swedish dish",       "Made w/ blood & flour",    "Often eaten w/ lingons"),
        ("surströmming","fermented herring",   "food", "HARD",   "Swedish specialty",  "Strong smell",             "Northern tradition"),
        ("rakknäckebröd","thin crispbread",    "food", "HARD",   "Crispy & dry",       "Typical Swedish bread",    "Made from rye"),
        ("färskpotatis","new potatoes",        "food", "HARD",   "Early-harvested",    "Tender skin",              "Popular at Midsummer"),
        ("gravlax",     "cured salmon",        "food", "HARD",   "Marinated w/ dill",  "Served thinly sliced",     "Traditional appetizer")
    ]

    with connect() as cur:

        insert_sql = """
            INSERT INTO words
                (swedish, english, category, difficulty, hint1, hint2, hint3)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        cur.executemany(insert_sql, words_data)

    print("Successfully inserted 60 items into 'words' table!")

if __name__ == "__main__":
    seed_words_with_hints()
