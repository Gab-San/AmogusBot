

__title__ = "GameLogic"


class Player:
    def __init__(self, name, num):
        self.name = name
        self.num = num

    def __str__(self) -> str:
        return f'{self.name}'