from dataclasses import dataclass

@dataclass
class Position:

    x: int
    y: int

    def move(self, x, y):
        self.x = x
        self.y = y