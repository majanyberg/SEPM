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
        # ================== CLOTHING (60 total) ==================
        # 20 EASY
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
        ("bälte",       "belt",                 "clothing", "EASY",   "Worn around waist",     "Holds up pants",          "Fashion accessory"),
        ("keps",        "cap",                  "clothing", "EASY",   "Headwear",              "Has a visor",             "Casual wear"),
        ("shorts",      "shorts",               "clothing", "EASY",   "Short pants",           "Worn in summer",          "Casual wear"),
        ("pyjamas",     "pajamas",              "clothing", "EASY",   "Sleepwear",             "Worn at night",           "Comfortable"),
        ("kappa",       "coat",                 "clothing", "EASY",   "Outerwear",             "Longer than jacket",      "Worn in cold weather"),
        ("underkläder", "underwear",            "clothing", "EASY",   "Worn under clothes",    "Various types",           "Daily wear"),
        ("jeans",       "jeans",                "clothing", "EASY",   "Denim pants",           "Casual wear",             "Blue color"),
        ("blus",        "blouse",               "clothing", "EASY",   "Women's top",           "Dressy",                  "Various styles"),
        ("väst",        "vest",                 "clothing", "EASY",   "Sleeveless garment",    "Worn over shirt",         "Fashionable"),
        ("träningsbyxor", "sweatpants",         "clothing", "EASY",   "Casual pants",          "Comfortable",             "Worn for exercise"),

        # 20 MEDIUM
        ("handskar",    "gloves",               "clothing", "MEDIUM", "Cover entire hand",     "Separate fingers",         "Worn in cold weather"),
        ("skjorta",     "shirt",                "clothing", "MEDIUM", "Collared top",          "Buttons on front",         "Unisex garment"),
        ("kostym",      "suit",                 "clothing", "MEDIUM", "Formal attire",         "Matching jacket & pants",  "Worn on special occasions"),
        ("hatt",        "hat",                  "clothing", "MEDIUM", "Headwear with a brim",  "Fashion or shade",         "Various styles"),
        ("halsduk",     "scarf",                "clothing", "MEDIUM", "Long fabric strip",     "Worn around neck",         "Keeps you warm"),
        ("kavaj",       "blazer",               "clothing", "MEDIUM", "Formal jacket",         "Worn with suit",           "Dressy"),
        ("väst",        "vest",                 "clothing", "MEDIUM", "Sleeveless garment",    "Worn over shirt",          "Fashionable"),
        ("overall",     "overalls",             "clothing", "MEDIUM", "One-piece garment",     "Worn for work",            "Durable"),
        ("regnbyxor",   "rain pants",           "clothing", "MEDIUM", "Waterproof pants",      "Worn in rain",             "Protects from wet"),
        ("badrock",     "bathrobe",             "clothing", "MEDIUM", "Worn after bath",       "Absorbent",                "Comfortable"),
        ("träningsjacka", "track jacket",       "clothing", "MEDIUM", "Worn for exercise",     "Lightweight",              "Zippered front"),
        ("kängor",      "boots",                "clothing", "MEDIUM", "Sturdy footwear",       "Covers ankle",             "Worn in winter"),
        ("leggings",    "leggings",             "clothing", "MEDIUM", "Tight-fitting pants",   "Stretchy material",        "Worn for exercise"),
        ("tunika",      "tunic",                "clothing", "MEDIUM", "Long top",              "Worn by women",            "Various styles"),
        ("cardigan",    "cardigan",             "clothing", "MEDIUM", "Buttoned sweater",      "Worn over shirt",          "Knitted"),
        ("polotröja",   "turtleneck",           "clothing", "MEDIUM", "High-necked sweater",   "Worn in winter",           "Warm"),
        ("kappa",       "overcoat",             "clothing", "MEDIUM", "Long coat",             "Worn in winter",           "Formal"),
        ("träningsskor", "sneakers",            "clothing", "MEDIUM", "Casual shoes",          "Worn for exercise",        "Comfortable"),
        ("hårband",     "headband",             "clothing", "MEDIUM", "Worn on head",          "Keeps hair back",          "Fashion accessory"),
        ("baddräkt",    "swimsuit",             "clothing", "MEDIUM", "Worn for swimming",     "One-piece or two-piece",   "Various styles"),

        # 20 HARD
        ("kalsonger",   "underpants (men)",     "clothing", "HARD",   "Men’s underwear",       "Worn under pants",         "Daily garment"),
        ("trosor",      "underpants (women)",   "clothing", "HARD",   "Women’s underwear",     "Cotton or lace",           "Daily garment"),
        ("strumpbyxor", "tights/pantyhose",     "clothing", "HARD",   "Sheer or thick",        "Waist to feet",            "Often worn with skirts"),
        ("regnjacka",   "rain jacket",          "clothing", "HARD",   "Waterproof coat",       "Used in wet weather",      "Often has a hood"),
        ("badbyxor",    "swim trunks",          "clothing", "HARD",   "Men’s swimwear",        "Used for swimming",        "Also called swim shorts"),
        ("fluga",       "bow tie",              "clothing", "HARD",   "Neckwear",              "Formal occasions",         "Tied in a bow"),
        ("halsband",    "necklace",             "clothing", "HARD",   "Worn around neck",      "Jewelry",                  "Various styles"),
        ("örhängen",    "earrings",             "clothing", "HARD",   "Worn on ears",          "Jewelry",                  "Various styles"),
        ("armband",     "bracelet",             "clothing", "HARD",   "Worn on wrist",         "Jewelry",                  "Various styles"),
        ("slips",       "tie",                  "clothing", "HARD",   "Neckwear",              "Formal occasions",         "Tied in a knot"),
        ("väst",        "waistcoat",            "clothing", "HARD",   "Sleeveless garment",    "Worn with suit",           "Formal"),
        ("korsett",     "corset",               "clothing", "HARD",   "Tight-fitting garment", "Shapes the torso",         "Worn by women"),
        ("strumpor",    "stockings",            "clothing", "HARD",   "Worn on legs",          "Sheer or opaque",          "Often worn with skirts"),
        ("kappa",       "cape",                 "clothing", "HARD",   "Sleeveless outerwear",  "Worn over shoulders",      "Fashionable"),
        ("hårnät",      "hairnet",              "clothing", "HARD",   "Worn on hair",          "Keeps hair in place",      "Used in food service"),
        ("hårspänne",   "hairpin",              "clothing", "HARD",   "Used to secure hair",   "Small accessory",          "Various styles"),
        ("halsduk",     "shawl",                "clothing", "HARD",   "Worn around shoulders", "Keeps warm",               "Fashionable"),
        ("kappa",       "cloak",                "clothing", "HARD",   "Long outer garment",    "Worn over clothes",        "Historical or fantasy"),
        ("hårband",     "hairband",             "clothing", "HARD",   "Worn on head",          "Keeps hair back",          "Fashion accessory"),
        ("baddräkt",    "bikini",               "clothing", "HARD",   "Two-piece swimsuit",    "Worn for swimming",        "Various styles"),

        # ================== FURNITURE (60 total) ==================
        # 20 EASY
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
        ("hylla",       "shelf",                "furniture", "EASY",   "Flat surface",          "Used for storage",         "Mounted on wall"),
        ("skåp",        "cabinet",              "furniture", "EASY",   "Storage unit",          "Has doors",                "Used in kitchen"),
        ("soffbord",    "coffee table",         "furniture", "EASY",   "Low table",             "Placed in living room",    "Used for drinks"),
        ("tv-bänk",     "tv stand",             "furniture", "EASY",   "Holds a television",    "Sometimes has storage",    "Usually in living room"),
        ("skrivbord",   "desk",                 "furniture", "EASY",   "Work surface",          "Often has drawers",        "Used for studying"),
        ("bokhylla",    "bookshelf",            "furniture", "EASY",   "Holds books",           "Multiple shelves",         "Wood or metal"),
        ("nattduksbord","nightstand",           "furniture", "EASY",   "Beside the bed",        "Holds lamp/alarm clock",   "May have drawers"),
        ("pall",        "stool",                "furniture", "EASY",   "Seat without back",     "Often wooden",             "Can be tall or short"),
        ("skoställ",    "shoe rack",            "furniture", "EASY",   "Organizes shoes",       "Placed near entryway",     "Multiple tiers"),
        ("sideboard",   "sideboard",            "furniture", "EASY",   "Dining room storage",   "Holds plates/dishes",      "Often waist-high"),

        # 20 MEDIUM
        ("skrivbord",   "desk",                 "furniture", "MEDIUM", "Work surface",          "Often has drawers",        "Used for studying"),
        ("bokhylla",    "bookshelf",            "furniture", "MEDIUM", "Holds books",           "Multiple shelves",         "Wood or metal"),
        ("tv-bänk",     "tv stand",             "furniture", "MEDIUM", "Holds a television",    "Sometimes has storage",    "Usually in living room"),
        ("nattduksbord","nightstand",           "furniture", "MEDIUM", "Beside the bed",        "Holds lamp/alarm clock",   "May have drawers"),
        ("pall",        "stool",                "furniture", "MEDIUM", "Seat without back",     "Often wooden",             "Can be tall or short"),
        ("skoställ",    "shoe rack",            "furniture", "MEDIUM", "Organizes shoes",       "Placed near entryway",     "Multiple tiers"),
        ("sideboard",   "sideboard",            "furniture", "MEDIUM", "Dining room storage",   "Holds plates/dishes",      "Often waist-high"),
        ("klädhängare", "coat rack",            "furniture", "MEDIUM", "Hangs coats",           "Freestanding or wall",     "In hallway"),
        ("kista",       "chest/trunk",          "furniture", "MEDIUM", "Storage box",           "Lid on top",               "Traditional or decorative"),
        ("vitrin",      "display cabinet",      "furniture", "MEDIUM", "Glass doors",           "Shows fine dishes",        "Typically in dining area"),
        ("soffbord",    "coffee table",         "furniture", "MEDIUM", "Low table",             "Placed in living room",    "Used for drinks"),
        ("skänk",       "buffet",               "furniture", "MEDIUM", "Dining room storage",   "Holds serving dishes",     "Often waist-high"),
        ("fotpall",     "ottoman",              "furniture", "MEDIUM", "Footrest",              "Often padded",             "Used with armchair"),
        ("väggskåp",    "wall cabinet",         "furniture", "MEDIUM", "Mounted on wall",       "Used for storage",         "In kitchen or bathroom"),
        ("sängbord",    "bedside table",        "furniture", "MEDIUM", "Beside the bed",        "Holds lamp/alarm clock",   "May have drawers"),
        ("skohylla",    "shoe shelf",           "furniture", "MEDIUM", "Organizes shoes",       "Placed near entryway",     "Multiple tiers"),
        ("klädskåp",    "wardrobe",             "furniture", "MEDIUM", "Stores clothes",        "Has doors",                "In bedroom"),
        ("väggspegel",  "wall mirror",          "furniture", "MEDIUM", "Mounted on wall",       "Reflective surface",       "Used for grooming"),
        ("sittpuff",    "pouf",                 "furniture", "MEDIUM", "Soft seat",             "Often round",              "Used in living room"),
        ("skåp",        "cupboard",             "furniture", "MEDIUM", "Storage unit",          "Has doors",                "Used in kitchen"),

        # 20 HARD
        ("skoställ",    "shoe rack",            "furniture", "HARD",   "Organizes shoes",       "Placed near entryway",     "Multiple tiers"),
        ("sideboard",   "sideboard",            "furniture", "HARD",   "Dining room storage",   "Holds plates/dishes",      "Often waist-high"),
        ("klädhängare", "coat rack",            "furniture", "HARD",   "Hangs coats",           "Freestanding or wall",     "In hallway"),
        ("kista",       "chest/trunk",          "furniture", "HARD",   "Storage box",           "Lid on top",               "Traditional or decorative"),
        ("vitrin",      "display cabinet",      "furniture", "HARD",   "Glass doors",           "Shows fine dishes",        "Typically in dining area"),
        ("sänggavel",   "headboard",            "furniture", "HARD",   "Attached to bed",       "Supports pillows",         "Decorative"),
        ("skänk",       "buffet",               "furniture", "HARD",   "Dining room storage",   "Holds serving dishes",     "Often waist-high"),
        ("fotpall",     "ottoman",              "furniture", "HARD",   "Footrest",              "Often padded",             "Used with armchair"),
        ("väggskåp",    "wall cabinet",         "furniture", "HARD",   "Mounted on wall",       "Used for storage",         "In kitchen or bathroom"),
        ("sängbord",    "bedside table",        "furniture", "HARD",   "Beside the bed",        "Holds lamp/alarm clock",   "May have drawers"),
        ("skohylla",    "shoe shelf",           "furniture", "HARD",   "Organizes shoes",       "Placed near entryway",     "Multiple tiers"),
        ("klädskåp",    "wardrobe",             "furniture", "HARD",   "Stores clothes",        "Has doors",                "In bedroom"),
        ("väggspegel",  "wall mirror",          "furniture", "HARD",   "Mounted on wall",       "Reflective surface",       "Used for grooming"),
        ("sittpuff",    "pouf",                 "furniture", "HARD",   "Soft seat",             "Often round",              "Used in living room"),
        ("skåp",        "cupboard",             "furniture", "HARD",   "Storage unit",          "Has doors",                "Used in kitchen"),
        ("bänk",        "bench",                "furniture", "HARD",   "Long seat",             "For multiple people",      "Often wooden"),
        ("väggklocka",  "wall clock",           "furniture", "HARD",   "Mounted on wall",       "Shows time",               "Decorative"),
        ("sängram",     "bed frame",            "furniture", "HARD",   "Supports mattress",     "Wood or metal",            "In bedroom"),
        ("skärmvägg",   "room divider",         "furniture", "HARD",   "Separates spaces",      "Portable",                 "Decorative"),
        ("vägglampa",   "wall lamp",            "furniture", "HARD",   "Mounted on wall",       "Provides light",           "Electric device"),

        # ================== FOOD (60 total) ==================
        # 20 EASY
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
        ("päron",       "pear",                "food", "EASY",   "Fruit",              "Green or yellow",          "Sweet and juicy"),
        ("apelsin",     "orange",              "food", "EASY",   "Citrus fruit",       "Orange peel",              "Rich in vitamin C"),
        ("jordgubbe",   "strawberry",          "food", "EASY",   "Berry",              "Red and sweet",            "Grows in summer"),
        ("vattenmelon", "watermelon",          "food", "EASY",   "Large fruit",        "Green outside",            "Red inside"),
        ("vindruvor",   "grapes",              "food", "EASY",   "Small fruit",        "Green or purple",          "Grows in clusters"),
        ("citron",      "lemon",               "food", "EASY",   "Citrus fruit",       "Yellow peel",              "Sour taste"),
        ("lök",         "onion",               "food", "EASY",   "Vegetable",          "Strong flavor",            "Used in cooking"),
        ("paprika",     "bell pepper",         "food", "EASY",   "Vegetable",          "Red, green, or yellow",    "Sweet taste"),
        ("broccoli",    "broccoli",            "food", "EASY",   "Green vegetable",    "Tree-like shape",          "Rich in vitamins"),
        ("spenat",      "spinach",             "food", "EASY",   "Leafy green",        "Rich in iron",             "Used in salads"),

        # 20 MEDIUM
        ("kanelbulle",  "cinnamon bun",        "food", "MEDIUM", "Swedish pastry",     "Cinnamon flavor",          "Coffee accompaniment"),
        ("köttbullar",  "meatballs",           "food", "MEDIUM", "Swedish dish",       "Often with lingonberries", "Minced meat mixture"),
        ("lax",         "salmon",              "food", "MEDIUM", "Fish",               "Pink/orange flesh",        "High in omega-3"),
        ("kyckling",    "chicken",             "food", "MEDIUM", "Poultry",            "White meat",               "Widely consumed"),
        ("lingonsylt",  "lingonberry jam",     "food", "MEDIUM", "Tart jam",           "Served with meat",         "Made from red berries"),
        ("räksmörgås",  "shrimp sandwich",     "food", "MEDIUM", "Open-faced sandwich","Topped with shrimp",       "Popular in Sweden"),
        ("falukorv",    "Falu sausage",        "food", "MEDIUM", "Swedish sausage",    "Large and ring-shaped",    "Often fried or baked"),
        ("pannkakor",   "pancakes",            "food", "MEDIUM", "Thin and flat",      "Served with jam",          "Popular dessert"),
        ("ärtsoppa",    "pea soup",            "food", "MEDIUM", "Thick soup",         "Made from yellow peas",    "Often served with pancakes"),
        ("knäckebröd",  "crispbread",          "food", "MEDIUM", "Dry and crispy",     "Made from rye",            "Common in Sweden"),
        ("gravad lax",  "gravlax",             "food", "MEDIUM", "Cured salmon",       "Marinated with dill",      "Served thinly sliced"),
        ("köttfärssås", "meat sauce",          "food", "MEDIUM", "Ground meat sauce",  "Often served with pasta",  "Similar to Bolognese"),
        ("sill",        "herring",             "food", "MEDIUM", "Pickled fish",       "Common in Sweden",         "Served with potatoes"),
        ("smörgåstårta","sandwich cake",       "food", "MEDIUM", "Layered sandwich",   "Decorated with toppings",  "Served at celebrations"),
        ("kräftor",     "crayfish",            "food", "MEDIUM", "Freshwater crustacean","Eaten at crayfish parties","Boiled with dill"),
        ("renskav",     "reindeer stew",       "food", "MEDIUM", "Sliced reindeer meat","Cooked with onions",       "Served with mashed potatoes"),
        ("prinskorv",   "prince sausage",      "food", "MEDIUM", "Small sausages",     "Often fried",              "Served at Christmas"),
        ("blåbärssoppa","blueberry soup",      "food", "MEDIUM", "Sweet soup",         "Made from blueberries",    "Served hot or cold"),
        ("kalops",      "beef stew",           "food", "MEDIUM", "Swedish beef stew",  "Cooked with onions",       "Served with potatoes"),
        ("risgrynsgröt","rice pudding",        "food", "MEDIUM", "Creamy dessert",     "Made from rice",           "Served with cinnamon"),
        
        # 20 HARD
        ("blodpudding", "blood pudding",        "food", "HARD",   "Swedish dish",       "Made w/ blood & flour",    "Often eaten w/ lingons"),
        ("surströmming","fermented herring",    "food", "HARD",   "Swedish specialty",  "Strong smell",             "Northern tradition"),
        ("rakknäckebröd","thin crispbread",     "food", "HARD",   "Crispy & dry",       "Typical Swedish bread",    "Made from rye"),
        ("färskpotatis","new potatoes",         "food", "HARD",   "Early-harvested",    "Tender skin",              "Popular at Midsummer"),
        ("gravlax",     "cured salmon",         "food", "HARD",   "Marinated w/ dill",  "Served thinly sliced",     "Traditional appetizer"),
        ("kräftor",     "crayfish",             "food", "HARD",   "Freshwater crustacean","Eaten at crayfish parties","Boiled with dill"),
        ("renskav",     "reindeer stew",        "food", "HARD",   "Sliced reindeer meat","Cooked with onions",       "Served with mashed potatoes"),
        ("prinskorv",   "prince sausage",       "food", "HARD",   "Small sausages",     "Often fried",              "Served at Christmas"),
        ("blåbärssoppa","blueberry soup",       "food", "HARD",   "Sweet soup",         "Made from blueberries",    "Served hot or cold"),
        ("kalops",      "beef stew",            "food", "HARD",   "Swedish beef stew",  "Cooked with onions",       "Served with potatoes"),
        ("risgrynsgröt","rice pudding",         "food", "HARD",   "Creamy dessert",     "Made from rice",           "Served with cinnamon"),
        ("palt",        "potato dumplings",     "food", "HARD",   "Swedish dish",       "Made from potatoes",       "Filled with pork"),
        ("svartsoppa",  "black soup",           "food", "HARD",   "Swedish soup",       "Made with blood",          "Served at special occasions"),
        ("lutfisk",     "lye fish",             "food", "HARD",   "Dried fish",         "Rehydrated with lye",      "Traditional Christmas dish"),
        ("ostkaka",     "cheesecake",           "food", "HARD",   "Swedish dessert",    "Made with curd cheese",    "Served with jam"),
        ("mandelmassa","almond paste",          "food", "HARD",   "Sweet paste",        "Made from almonds",        "Used in baking"),
        ("semla",       "cream bun",            "food", "HARD",   "Swedish pastry",     "Filled with cream",        "Eaten on Fat Tuesday"),
        ("pepparkakor", "gingerbread cookies",  "food", "HARD",   "Swedish cookies",    "Spiced with ginger",       "Eaten at Christmas"),
        ("julskinka",   "Christmas ham",        "food", "HARD",   "Swedish dish",       "Baked ham",                "Served at Christmas"),
        ("glögg",       "mulled wine",          "food", "HARD",   "Spiced wine",        "Served hot",               "Popular at Christmas")
    ]

    with connect() as cur:

        insert_sql = """
            INSERT INTO words
                (swedish, english, category, difficulty, hint1, hint2, hint3)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT DO NOTHING
        """
        cur.executemany(insert_sql, words_data)

    print("Successfully inserted items into 'words' table!")

if __name__ == "__main__":
    seed_words_with_hints()
