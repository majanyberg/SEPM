from dataclasses import dataclass

from backend.Position import Position

@dataclass
class ClothingItem:

        name: str
        adjectives: list[str]
        clothingPosition: Position
        wordPosition: Position
