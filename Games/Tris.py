###### TRIS PROJECT ######

__title__ = 'Tris'

import GameLogic

"""
    Disegnare lo schema del tris, da fare su bot discord sul messaggio inviato.
    Impostando una Matrice tre per tre, per ogni mossa, è necessario:
        1. Leggere da input formattato la mossa del giocatore.
        2. Controllare che la mossa sia valida. 
        3. Salvare la risposta sulla matrice.
        4. Disegnare sulla matrice la risposta ((Discord Bot)).
        5. Controllare le condizioni di vittoria.
        6. Nominare, elogiare il vincitore((Discord Bot)).
"""

"""
    Definire una classe tris in cui sono definite tutte le funzioni e attributi utili per lavorare con una matrice di tris.
    È possibile implementare:
        - [Low] Nome/Codice della matrice (per avere più istanze e ricordarsi le vecchie partite)
        > CHK [High] Mossa Successiva 
        > CHK [High] Controllo della mossa
        - [Medium] Reset della matrice
        - [High] Eliminiazione della matrice una volta finita la partita 

"""

class TrisPlayer(GameLogic.Player):
    def __init__(self, name, number, character):
        super().__init__(name, number)
        self.character = character
    
    def __str__(self) -> str:
        return f'{self.name} is playing with {self.character}'


def ParseInput(input_move) -> tuple:
    input_move = input_move.strip()

    if len(input_move) != 2:
        raise SyntaxError("Wrong Movement Format")
    

    match input_move[0].lower():
        case 'a': column = 0
        case 'b': column = 1
        case 'c': column = 2
        case _: raise Exception("Move out of bounds")

    match input_move[1].lower():
        case '1': row = 0
        case '2': row = 1
        case '3': row = 2
        case _: raise Exception("Move out of bounds")

    return (row, column)


def Endgame(playerid) -> None:
    print(f'{playerid.upper()} WON THE GAME!')
    exit()

class TrisMatch:

    characters = ['X','O']

    def __init__(self) -> None:
        self.matrix = [[0,0,0],[0,0,0],[0,0,0]]; # Initializing current Tris Matrix #
        self.players = []

    def RegisterPlayers(self) -> None:
        for i in range (1,3):
            currPl_name = input(f'Player #{i}: ')
            self.players.append(TrisPlayer(currPl_name, i, self.characters[i-1]))
        
        for _ in self.players:
            print(_)
            
        print("\n")
    
    def ChangePlayer(self, player_number) -> int:
        player_number = (player_number + 1) % 2
        return player_number

    def PlayMove(self, currentMove, character) -> None:
        # verifying if the move is plausible #
        if(self.matrix[currentMove[0]][currentMove[1]] != 0 ):
            raise Exception("Occupied Tile")
        
        self.matrix[currentMove[0]][currentMove[1]] = character

        for i in range (0,3):
            for j in range (0,3):
                print(f'[{self.matrix[i][j]}] at {i},{j}')
            print("\n")
      
    
    def CheckWinner(self, player, sign) -> None:
        if (self.matrix[0][0] == sign and self.matrix[0][1] == sign and self.matrix[0][2] == sign):
            Endgame(player.name)
        if(self.matrix[0][0] == sign and self.matrix[1][1] == sign and self.matrix[2][2] == sign):
            Endgame(player.name)
        if(self.matrix[0][0] == sign and self.matrix[1][0] == sign and self.matrix[2][0] == sign):
            Endgame(player.name)
        if(self.matrix[0][1] == sign and self.matrix[1][1] == sign and self.matrix[2][1] == sign):
            Endgame(player.name)
        if(self.matrix[0][2] == sign and self.matrix[1][2] == sign and self.matrix[2][2] == sign):
            Endgame(player.name)
        if(self.matrix[0][2] == sign and self.matrix[1][1] == sign and self.matrix[2][0] == sign):
            Endgame(player.name)
        if(self.matrix[1][0] == sign and self.matrix[1][1] == sign and self.matrix[1][2] == sign):
            Endgame(player.name)
        if(self.matrix[2][0] == sign and self.matrix[2][1] == sign and self.matrix[2][2] == sign):
            Endgame(player.name)
        


# REDO THE WINNING CONDITION #

# Game Logic#
def main() -> None:

    GameLogic.StartNewGame()

    while True:
        tris = TrisMatch()
        tris.RegisterPlayers()
        nextPlayer = 0

        while True:
            print(f'{tris.players[nextPlayer]}\n')

            while True:
                try:
                    while True:
                        nextMove = input("Which tile do u wanna mark?\n\n")
                        try:
                            nextMove = ParseInput(nextMove)
                            break
                        except (SyntaxError, Exception) as err:
                            print(f'{err}: Correct format is [letter][number]\n' +
                                  "letter must be either a, b or c\nnumber must be a number between 1 and 3\n")
                    print(str(nextMove) + "\n")
                    tris.PlayMove(nextMove, tris.players[nextPlayer].character)
                    break
                except Exception as error:
                    print(f'Error: {error}... Choose another move\n')
    
            tris.CheckWinner(tris.players[nextPlayer], tris.players[nextPlayer].character)
            nextPlayer = tris.ChangePlayer(nextPlayer)





if __name__ == "__main__":
    main()