"""Po wyświeleniu komunikatu z informacją o biciu, 
użytkownik programu, powinien mieć możliwość:
1) wylosowania nowej pozycji dla pionka z pozostawieniem pierwotnego układu hetmanów;
2) usunięcia dowolnego hetmana (wskazanie jego pozycji);
3) ponowną weryfikację bicia po ustaleniu zmian."""
import random

from ex2_move import pawn_situation, row_pawn, col_pawn, pawn_placement, queen_placements
from ex1_create_board import chess_board, display_board


def remove_current_pawn(chess_board):
    '''Function to remove existng pawn 'P' from chess board'''

    # Remove existng pawn - change |P|->| |
    for row in range(8):
          for col in range(8):
            # Place Pawn if field is empty
            if chess_board[row][col] == '|P|':
                chess_board[row][col]= '| |'
    return chess_board

def board_new_place_pawn(chess_board):
        '''Random placement of single Pawn 'P'  '''
        
        # Select new random place
        new_row = random.randint(0, 7)
        new_col = random.randint(0, 7)
        for row in range(8):
          for col in range(8):
            # Place Pawn if field is empty
            if chess_board[new_row][new_col] != '|H|':
                    chess_board[new_row][new_col] = '|P|'
        return chess_board

def current_position_pawn(chess_board):
    '''Function to get current postion of single Pawn 'P'  '''

    for row in range(8):
          for col in range(8):
            # Place Pawn if field is empty
            if chess_board[row][col] == '|P|':
                row_new_pawn = chess_board[row]
                col_new_pawn = chess_board[col]
                current_location_pawn = (row_new_pawn, col_new_pawn)
    return current_location_pawn

def remove_queen(queen_placements, r_queen_row, r_queen_col):
    
    print(f"Remove queen in row: {r_queen_row}")
    print(f"Remove queen in col: {r_queen_col}")
    remove_queen_position = (r_queen_row, r_queen_col)
    print(remove_queen_position)

    new_queen_placements = [tup for tup in queen_placements if tup != remove_queen_position]
    print(f"New queen positions: {new_queen_placements}")
    return new_queen_placements


def is_attacked_new():
    pass

def menu():

    while True:
        print("1. Choose a new placement for pawn.")
        print("2. Remove queen on pointed placement")
        print("3. Check if pawn in location is attacked by queen?")
        print("4. Quit")
        choice = input("Choose option: ")

        if choice == "1":
            print("You choose 1 -  Choose a new placement for pawn.")
            print("Here is new placement for pawn")
            board_without_pawn= remove_current_pawn(chess_board)
            chess_board_new_place_pawn = board_new_place_pawn(board_without_pawn)
            display_board(chess_board_new_place_pawn)

        elif choice == "2":
            print("\nYou choose 2 - Remove queen on pointed placement")
            print(f"Actual queen position: {queen_placements}")
            r_queen_row = int(input("Which queen do you want to remove?type row:"))
            r_queen_col = int(input("Which queen do you want to remove?type col:"))
            new_queen_placements = remove_queen(queen_placements, r_queen_row, r_queen_col)

        elif choice == "3":
            print("You choose 3 - Check if pawn in location is attacked by queen?")
            position_pawn = current_position_pawn(chess_board_new_place_pawn)
            print(f"Current position of pawn: {position_pawn}")
        elif choice == "4":
            print("You quit")
            break
        else:
            print("Wrong choice. Try again.")


def show_menu(pawn_situation):
    print(f"\nPawn can be attacked? {pawn_situation}")
    menu()

show_menu(pawn_situation)
