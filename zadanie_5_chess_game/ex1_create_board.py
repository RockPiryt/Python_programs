'''Generowanie mapy [3 pkt]
Pierwszy etapem zadania będzie wygenerowanie planszy 8x8. 
W skład mapy wychodzą:
- k hetmanów rozmieszczonych losowa na mapie,
- jeden pionek rozmieszczony losowa na mapie.
Każdy z elementów zostaje ustawiony na różnej pozycji. 
Po włączeniu programu schemat planszy powinien się wyświetlać 
użytkownikowi.'''

import random

def display_board(board):
    '''Print chess board with paws and queens'''
    for row in board:
        print("".join(row))#join elements on list

def create_empty_board():
        '''Create matrix with list comprehension'''

        my_game_board = [['|_|' if field % 2 == 0  else '|#|' for field in range(8)] if field % 2==0  \
                        else ['|#|' if field % 2 == 0  else '|_|' for field in range(8)] \
                        for field in range(8)]
        return my_game_board

def place_queen(board):
        '''Random placement of Queens 'H' (max 5 Queens)'''

        # Random quantity of Queen
        num_queens = random.randint(1, 5)
        for field in range(num_queens):
                row = random.randint(0, 7)
                col = random.randint(0, 7)
                board[row][col] = '|H|'

def place_pawn(board):
        '''Random placement of single Pawn 'P'  '''
        
        # Select random placement 
        row = random.randint(0, 7)
        col = random.randint(0, 7)
        # Place Pawn if field is empty
        if board[row][col] != '|H|':
                board[row][col] = '|P|'

chess_board = create_empty_board()

place_queen(chess_board)
place_pawn(chess_board)

display_board(chess_board)

