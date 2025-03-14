from dataclasses import dataclass

from backend.Character import Character

@dataclass
class Level:

    levelName: str
    character: Character
    nouns: list[str]
    adjectives: list[str]
