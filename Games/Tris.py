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
        - [High] Mossa Successiva
        - [High] Controllo della mossa
        - [Medium] Reset della matrice
        - [High] Elminiazione della matrice una volta finita la partita 

"""



def ParseInput(input_move) -> tuple:
    input_move = input_move.strip()

    if len(input_move) != 2 and input_move[0].lower() not in ['a', 'b', 'c'] and input_move[1] not in ['1', '2', '3']:
        raise Exception("Wrong Movement Format")
    

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



def StartNewGame() -> None:
    confirmStart = input("Premere [Y] per iniziare una nuova partita" + "\n" + 
                         "Premere [N] per interrompere\n\n")
    
    if(confirmStart == 'N'): exit()

def __CheckWinner() -> None:
    exit()



class TrisMatch:
    def __init__(self) -> None:
        self.matrix = [[0,0,0],[0,0,0],[0,0,0]]; # Initializing current Tris Matrix #
        self.players = []

    def RegisterPlayers(self) -> None:
        for i in range (1,3):
            currPl_name = input(f'Giocatore numero {i}: ')
            self.players.append(GameLogic.Player(currPl_name, i))
        
        for _ in self.players:
            print(_)
            
        print("\n")
       

    def PlayMove(self, currentMove, player_number) -> int:
        # verifying if the move is plausible #
        if(self.matrix[currentMove[0]][currentMove[1]] != 0 ):
            raise Exception("Occupied Tile")
        
        self.matrix[currentMove[0]][currentMove[1]] = player_number

        player_number = (player_number + 1) % 2
        return player_number






# Game Logic#
def main() -> None:

    StartNewGame()

    while True:
        tris = TrisMatch()
        tris.RegisterPlayers()
        nextPlayer = 0

        while True:
            print(f'Gioca {tris.players[nextPlayer]}\n')
            nextMove = input("Quale casella vuoi occupare?\n\n")
            nextMove = ParseInput(nextMove)
            print(str(nextMove) + "\n")
            nextPlayer = tris.PlayMove(nextMove, nextPlayer)







if __name__ == "__main__":
    main()