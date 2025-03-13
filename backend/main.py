import os
from pathlib import Path

from backend.Character import Character
from backend.ClothingItem import ClothingItem
from backend.Position import Position
from backend.Level import Level

import pickle

def saveLevel(levelName, character, nouns, adjectives):
    levelName = "Level 1"
    level = Level((levelName), getCharacter(), getNouns(), getAdjectives())
    with open(f"levels/{levelName}.lvl", "wb") as f:
        pickle.dump(level, f)

def getLevel(levelName):
    with open(f"levels/{levelName}.lvl", "rb") as f:
        level = pickle.load(f)
    return level

def getCharacter():
    clothes = []
    clothes.append(ClothingItem("Hatt", ["Grå", "Grå1"], Position(80, 200), Position(190, 195)))
    clothes.append(ClothingItem("Kavaj", ["Randig1"], Position(107, 290), Position(215, 255)))
    clothes.append(ClothingItem("Handske", ["Blå"], Position(85, 353), Position(220, 315)))
    clothes.append(ClothingItem("Byxor", ["Rutig2", "Rosa"], Position(100, 375), Position(215, 370)))
    return Character(clothes, "characters/hen1.png")

def getNouns():
    return ["Hatt", "Kavaj", "Klänning", "Kjol", "Solhatt",
            "Hoodie", "Väst", "Klacksko", "Handske", "Sandal",
            "Shorts", "Byxor", "Kavaj2", "Klänning2", "Kjol2", "Solhatt2",
            "Hoodie2", "Väst2", "Klacksko2", "Handske2", "Sandal2"]

def getAdjectives():
    return ["Grå", "Randig", "Blå", "Rutig", "Rosa",
            "Grå1", "Randig1", "Blå1", "Rutig1", "Rosa1",
            "Grå2", "Randig2", "Blå2", "Rutig2", "Rosa2",
            "Grå3", "Randig3", "Blå3", "Rutig3", "Rosa3",]

def validateAnswer(character, answer):
    clothes = character.clothes
    success = True
    
    clothingNamesAndAdjectives = []
    for clothingItem in clothes:
        clothingNamesAndAdjectives.extend(clothingItem.adjectives)
        clothingNamesAndAdjectives.append(clothingItem.name)

    for i, word in enumerate(answer):
        success = success and word == clothingNamesAndAdjectives[i]

    return success

def getLevelNames():
    file_names = os.listdir("levels")
    cleaned_names = [Path(f).stem for f in file_names]
    return cleaned_names

def levelExists(levelName):
    return levelName in getLevelNames()

def getCharacterPaths():
    return os.listdir("characters")