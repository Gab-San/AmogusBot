

__title__ = "GameLogic"



def StartNewGame() -> None:
    confirmStart = input("Press [Y] to start a new game\n" + 
                         "Press [N] to stop\n\n")
    
    if(confirmStart.upper() != 'Y'):
        exit("We'll play togheter another time!!")


def Endgame(playerid) -> None:
    print(f'{playerid.upper()} WON THE GAME!')


class Game:
    def __init__(self, player_number):
        self.players = []
        self.player_number = player_number

class Player:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self) -> str:
        return f'{self.name} is player {self.number}'
    