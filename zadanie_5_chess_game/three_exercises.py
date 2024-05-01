'''Generowanie mapy [3 pkt]
Pierwszy etapem zadania będzie wygenerowanie planszy 8x8. 
W skład mapy wychodzą:
- k hetmanów rozmieszczonych losowa na mapie,
- jeden pionek rozmieszczony losowa na mapie.
Każdy z elementów zostaje ustawiony na różnej pozycji. 
Po włączeniu programu schemat planszy powinien się wyświetlać 
użytkownikowi.'''

'''''Weryfikacja bicia [4 pkt]
Program powinien odpowiadać na pytania: Czy pionek zostanie zbity
przez któregoś z hetmanów?

Dodakowo: wyświetlić pozycje wszystkich hetmanów, 
którzy mają możliwość zbicia pionka (o ile tacy istnieją).'''

import random

# First exercise_________________________________________
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

# Secoond exercise__________________________________________________

def position_queens(board):
     '''Get positions of all generated queens'''

     positions_queens_list = []

     for row in range(8):
          for col in range(8):
               if board[row][col] == '|H|':
                    row_queen = row
                    col_queen = col
                    single_position_queen = (row_queen, col_queen)
                    positions_queens_list.append(single_position_queen)

     return positions_queens_list


queen_placements = position_queens(chess_board)#list with tuples
print(f"Queens positions on chess board: {queen_placements}")
#[(0, 1), (1, 4), (4, 1)]

# rows_queen_list = []
# cols_queen_list = []

# for tuple_item in queen_placements:
#       row_queen = tuple_item[0]
#       rows_queen_list.append(row_queen)

#       col_queen = tuple_item[1]
#       cols_queen_list.append(col_queen)


def position_pawn(board):
     '''Get single pawn postion'''

     for row in range(8):
          for col in range(8):
               if board[row][col] == '|P|':
                    row_pawn = row
                    col_pawn = col
                    single_position_pawn = (row_pawn, col_pawn)
                    
     return single_position_pawn

pawn_placement = position_pawn(chess_board)#tuple
print(f"Pawn position on chess board: {pawn_placement}")
#(5, 7)

# Row and col of pawn
row_pawn = pawn_placement[0]
col_pawn = pawn_placement[1]


def is_attacked_by_queen(row_pawn, col_pawn, queen_placements):
    '''Function to check if queen can attack a pawn'''

    # Iterate for tuples on list
    for tuple_item in queen_placements:
        row_queen = tuple_item[0]
        col_queen = tuple_item[1]
        # Quenn can attack if it is on the same row, column or diagonal as pawn 
        if (row_pawn == row_queen or  col_pawn == col_queen or  
            abs(row_pawn - row_queen) == abs(col_pawn - col_queen)):
                print("yes") 
        else:
              print("no")
#     return (row_pawn == row_queen or  
#             col_pawn == col_queen or  
#             abs(row_pawn - row_queen) == abs(col_pawn - col_queen))  # Ta sama przekątna

# def find_attacking_queens(pawn_row, pawn_col, queens_positions):
#     attacking_queens = []
#     for queen_row, queen_col in queens_positions:
#         if is_attacked_by_queen(pawn_row, pawn_col, queen_row, queen_col):
#             attacking_queens.append((queen_row, queen_col))
#     return attacking_queens

# def display_attacking_queens(pawn_row, pawn_col, queens_positions):
#     attacking_queens = find_attacking_queens(pawn_row, pawn_col, queens_positions)
#     if attacking_queens:
#         print("Hetman(y) mogący zbić pionka na pozycji ({},{}):".format(pawn_row, pawn_col))
#         for queen_row, queen_col in attacking_queens:
#             print("({},{})".format(queen_row, queen_col))
#     else:
#         print("Żaden hetman nie może zbić pionka na pozycji ({},{}).".format(pawn_row, pawn_col))


# # Sprawdzenie czy pionek jest atakowany przez któregoś z hetmanów
# display_attacking_queens(pawn_placement[0], pawn_placement[1], queen_placements)

is_attacked_by_queen(row_pawn, col_pawn, queen_placements)

# def is_attacked_by_queen(row_pawn, col_pawn, row_queen, col_queen):
#     # Hetman może zbijać pionka jeśli znajduje się na tej samej kolumnie, wierszu lub po przekątnej
#     return (row_pawn == row_queen or  
#             col_pawn == col_queen or  
#             abs(row_pawn - row_queen) == abs(col_pawn - col_queen))  # Ta sama przekątna

# def find_attacking_queens(pawn_row, pawn_col, queens_positions):
#     attacking_queens = []
#     for queen_row, queen_col in queens_positions:
#         if is_attacked_by_queen(pawn_row, pawn_col, queen_row, queen_col):
#             attacking_queens.append((queen_row, queen_col))
#     return attacking_queens

# def display_attacking_queens(pawn_row, pawn_col, queens_positions):
#     attacking_queens = find_attacking_queens(pawn_row, pawn_col, queens_positions)
#     if attacking_queens:
#         print("Hetman(y) mogący zbić pionka na pozycji ({},{}):".format(pawn_row, pawn_col))
#         for queen_row, queen_col in attacking_queens:
#             print("({},{})".format(queen_row, queen_col))
#     else:
#         print("Żaden hetman nie może zbić pionka na pozycji ({},{}).".format(pawn_row, pawn_col))

# # Przykładowe pozycje hetmanów i pionka
# # queens_positions = [(1, 2), (3, 0), (4, 3), (6, 5)]
# # pawn_position = (5, 4)
# queens_positions = queen_placement
# pawn_position = pawn_placement

# # Sprawdzenie czy pionek jest atakowany przez któregoś z hetmanów
# display_attacking_queens(pawn_position[0], pawn_position[1], queens_positions)

