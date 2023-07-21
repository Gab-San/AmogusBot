

__title__ = "GameLogic"



def StartNewGame() -> None:
    confirmStart = input("Press [Y] to start a new game\n" + 
                         "Press [N] to stop\n\n")
    
    if(confirmStart.upper() != 'Y'):
        exit()





class Player:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self) -> str:
        return f'{self.name} is player #{self.number}'
    