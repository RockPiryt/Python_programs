"""Po wyświeleniu komunikatu z informacją o biciu, 
użytkownik programu, powinien mieć możliwość:
1) wylosowania nowej pozycji dla pionka z pozostawieniem pierwotnego układu hetmanów;
2) usunięcia dowolnego hetmana (wskazanie jego pozycji);
3) ponowną weryfikację bicia po ustaleniu zmian."""

from ex1_create_board import chess_board, display_board, place_pawn
from ex2_move_linear import get_position_pawn, get_position_queens, attacked_queen_postion, is_attacked_q, queen_placements, my_answer, create_final_list


def remove_current_pawn(chess_board):
    '''Function to remove existng pawn 'P' from chess board'''

    # Remove existng pawn - change |P|->| |
    for row in range(8):
          for col in range(8):
            # Place Pawn if field is empty
            if chess_board[row][col] == '|P|':
                chess_board[row][col]= '| |'
    return chess_board


def remove_userQueen(r_queen_row, r_queen_col):
    '''Function to create board without pointed queen.'''

    # Remove existng pawn - change |H|->| |
    for row in range(8):
          for col in range(8):
            # Place Pawn if field is empty
            if chess_board[r_queen_row][r_queen_col] == '|H|':
                chess_board[r_queen_row][r_queen_col]= '| |'
    return chess_board


def menu():

    while True:
        print("1. Choose a new placement for pawn.")
        print("2. Remove queen on pointed placement")
        print("3. Check if pawn in location is attacked by queen?")
        print("4. Quit")
        choice = input("Choose option: ")

        if choice == "1":
            print("You choose 1 -  Choose a new placement for pawn.")
            print("Here is new placement for pawn on board:")
            board_without_pawn = remove_current_pawn(chess_board)
            chess_board_new_place_pawn = place_pawn(board_without_pawn)
            display_board(chess_board_new_place_pawn)
            current_position_pawn = get_position_pawn(chess_board)
            print(f"New current position of pawn {current_position_pawn}\n")


        elif choice == "2":
            print("\nYou choose 2 - Remove queen on pointed placement")
            print(f"Actual queen position: {queen_placements}")
            r_queen_row = int(input("Which queen do you want to remove?type row:"))
            r_queen_col = int(input("Which queen do you want to remove?type col:"))
            user_queen_board = remove_userQueen(r_queen_row, r_queen_col)
            new_queen_placements = get_position_queens(user_queen_board)
            print(f"Actual queen position: {new_queen_placements}")
            display_board(user_queen_board)

        elif choice == "3":
            print("\nYou choose 3 - Check if pawn in location is attacked by queen")
            current_position_pawn = get_position_pawn(chess_board)
            current_positions_queen = get_position_queens(chess_board)
            current_attacked_queen_list = attacked_queen_postion(current_position_pawn, current_positions_queen)
            print(f"attacked_queen_list {current_attacked_queen_list}\n")
            # Function to get final queens
            closest_queens = create_final_list(current_attacked_queen_list)
            print("Closest queen current", closest_queens)
            # If final quenns list is not empty -> True answer
            curr_answer = is_attacked_q(closest_queens)
            print(f"\nIf pawn in current location is attacked by queens? {curr_answer}\n")

        elif choice == "4":
            print("You quit")
            break
        else:
            print("Wrong choice. Try again.")


def show_menu(answer):
    print(f"\nPawn can be attacked? {answer} \n")
    menu()

# show_menu(my_answer)
