from dataclasses import dataclass

from backend.ClothingItem import ClothingItem

@dataclass
class Character:
   
    clothes: list[ClothingItem]
    path_to_img: str