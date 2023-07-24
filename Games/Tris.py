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

# define constants #

MAX_ROW = 3
FIRST_COL = 'a'
MAX_PLAYERNUMBER = 2


def AlgebraicToComputer(input_move) -> tuple:
    input_move = input_move.strip()

    if len(input_move) != 2:
        raise SyntaxError("Wrong Movement Format")
    
    row = MAX_ROW - int(input_move[1]) # 3 - 1 = 2 which is the last row #
    col = ord(input_move[0].lower()) - ord(FIRST_COL)

    print(f'{(row,col)} is the move you chose')
    return (row, col)

def VerifyMove(input_move) -> tuple:
    if (input_move[0] < 0 or input_move[0] > 2) or (input_move[1] < 0 or input_move[1] > 2):
        raise ValueError("Move Out Of Bounds")

def __Endgame(playerid, end_condition) -> bool:
    
    match end_condition:
        case 0: GameLogic.Endgame(playerid)
        case 1: print(f'The game was tied')
        case _: print(f'For some reason the game has Ended')
    
    return True



class TrisPlayer(GameLogic.Player):
    def __init__(self, name, number, character):
        super().__init__(name, number)
        self.character = character
    
    def __str__(self) -> str:
        return f'{self.name} is playing with {self.character}'


class TrisMatch(GameLogic.Game):

    characters = ['X','O']

    def __init__(self, player_number) -> None:
        super().__init__(player_number)
        self.matrix = [[0,0,0],[0,0,0],[0,0,0]]; # Initializing current Tris Matrix #
        self.num_of_plays = 0

    def RegisterPlayers(self) -> None:
        for i in range (0, self.player_number):
            currPl_name = input(f'Player #{i + 1}: ')
            self.players.append(TrisPlayer(currPl_name, i, self.characters[i]))

        for _ in self.players:
            print(_)
        print("\n")
    
    def ChangePlayer(self, player_number) -> int:
        player_number = (player_number + 1) % 2
        return player_number

    def Place(self, currentMove, character) -> None:
        # Verifying if the move is possible #
        try:
            VerifyMove(currentMove)
        except ValueError as error:
            raise error
        
        if(self.matrix[currentMove[0]][currentMove[1]] != 0 ):
            raise Exception("Occupied Tile")
        
        # If the play is possible than complete the move #
        self.matrix[currentMove[0]][currentMove[1]] = character
        self.num_of_plays += 1 # Updating the number of moves (see isFull()) #

    def CheckWin(self, currentMove, char) -> bool:
        if(self.num_of_plays < 4): return False # With less than 4 moves it's impossible to win # 
        return self.__CheckWinRows(currentMove[0], char) or self.__CheckWinColumns(currentMove[1], char) or self.__CheckWinDiags(char)


    def __CheckWinRows(self, row, char) -> bool:
        for i in range (0,3):
            if(self.matrix[row][i] != char):
                return False
        return True # If loop arrives here it means that all char on the row were equal #
                

    def __CheckWinColumns(self, col, char) -> bool:
        for i in range (0,3):
            if(self.matrix[i][col] != char):
                return False
        return True # If loop arrives here it means that all char on the col were equal #
        

    def __CheckWinDiags(self, char) -> bool:
        return self.__CheckDirDiags(char) or self.__CheckIndDiags(char)
    
    def __CheckDirDiags(self, char) -> bool:
        for (i,j) in [(0,0), (1,1), (2,2)]:
            if(self.matrix[i][j] != char):
                return False
        return True
    
    def __CheckIndDiags(self, char) -> bool:
        for (i,j) in [(0,2), (1,1), (2,0)]:
            if(self.matrix[i][j] != char):
                return False
        return True

    def isFull(self) -> bool:
        return (self.num_of_plays >= 9)   

                




# REDO THE WINNING CONDITION #

# Game Logic#
def main() -> None:

    GameLogic.StartNewGame()
    gameHasEnded = False
    tris = TrisMatch(MAX_PLAYERNUMBER) 
    tris.RegisterPlayers()

    while not gameHasEnded:
        for i in tris.players :
            print(f'{i}\n')
            acceptedMove = False

            while not acceptedMove:
                currentMove = input("Which tile do you want to mark?\n\n")
                try:
                    currentMove = AlgebraicToComputer(currentMove)
                except SyntaxError as err:
                    print(f'{err}: Correct format is [letter][number]\n')
                    continue

                # At this point the move is in the correct format and has been translated #
                try:
                    tris.Place(currentMove, i.character)
                    acceptedMove = True
                except (ValueError, Exception) as err:
                    print(f'Error: {err}...\nChoose another move\n')
                    acceptedMove = False
            
            # At this point the move has been registered #

            if( tris.CheckWin(currentMove, i.character) ):
                gameHasEnded = __Endgame(i.name, 0) # 0 is the winning condition #
                break

            if( tris.isFull() ):
                gameHasEnded = __Endgame(i.name, 1) # 1 is the tie condition #
                break



if __name__ == "__main__":
    main()