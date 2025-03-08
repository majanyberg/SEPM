from backend.Character import Character
from backend.ClothingItem import ClothingItem
from backend.Position import Position

# TODO
def getCharacter(ID):
    clothes = []
    clothes.append(ClothingItem("Hatt", "Svart", "", Position(80, 200), Position(190, 195)))
    clothes.append(ClothingItem("Hatt", "Svart", "", Position(107, 290), Position(215, 255)))
    clothes.append(ClothingItem("Hatt", "Svart", "", Position(85, 343), Position(220, 315)))
    clothes.append(ClothingItem("Hatt", "Svart", "", Position(100, 375), Position(215, 370)))
    return Character(1, clothes, "frontend/assets/hen1.png")

# TODO
# CANNOT BE DUPLICATE WORDS
def getNouns(charachterID):
    return ["Hatt", "Kavaj", "Klänning", "Kjol", "Solhatt",
            "Hoodie", "Väst", "Klacksko", "Handske", "Sandal",
            "Shorts", "Byxor", "Kavaj2", "Klänning2", "Kjol2", "Solhatt2",
            "Hoodie2", "Väst2", "Klacksko2", "Handske2", "Sandal2"]

#TODO
def getAdjectives(henID):
    return ["Grå", "Randig", "Blå", "Rutig", "Rosa",
            "Grå1", "Randig1", "Blå1", "Rutig1", "Rosa1",
            "Grå2", "Randig2", "Blå2", "Rutig2", "Rosa2",
            "Grå3", "Randig3", "Blå3", "Rutig3", "Rosa3",]

# TODO
def validateAnswer(words):
    return words == ["Hatt", "Kavaj", "Handske", "Byxor"]