import pytest
from ex1_create_board import create_empty_board, place_pawn, place_queen, display_board

from ex2_move_linear import (get_position_queens, get_position_pawn, 
                             attacked_queen_postion, is_attacked_q, min_distance,
                             create_four_side_list_compre, create_win_queen, create_final_list)

from ex3_more import remove_current_pawn, remove_userQueen, menu

# ________________________________Test create random chess board
# Create empty chess board
@pytest.fixture()
def empty_board():
    print("\nTest empty chess board:")
    empty_board = create_empty_board()
    display_board(empty_board)
    return empty_board

# Create board with one pawn and random numbers of queens
@pytest.fixture()
def chess_board():
    print("\nTest chess board:")
    chess_board = create_empty_board()
    place_pawn(chess_board)
    place_queen(chess_board)
    display_board(chess_board)
    return chess_board

# __________________________________Create chess_board for tests
empty_chess_board = create_empty_board()
board_with_queen = place_queen(empty_chess_board)
test_board = place_pawn(board_with_queen)
print("Our test board")
display_board(test_board)

# ________________________________Fixtures to ex2
# Get location of pawn
@pytest.fixture()
def fix_pawn_placement():
    pawn_location = get_position_pawn(test_board)
    return pawn_location

# Get locations of queens
@pytest.fixture()
def fix_queen_locations_test():
    queen_locations = get_position_queens(test_board)
    return queen_locations

# Create attack queen list
@pytest.fixture()
def fix_attack_queens(fix_pawn_placement, fix_queen_locations_test):
    attack_queen_test = attacked_queen_postion(fix_pawn_placement, fix_queen_locations_test)
    return attack_queen_test

# Get minimal distance beetween queen and pawn
@pytest.fixture()
def fix_min_distance(fix_attack_queens):
    val_min_distance = min_distance(fix_attack_queens)
    return val_min_distance


# Create lists with queens on 4 side of pawn
@pytest.fixture()
def fix_create_four_sides_compre(fix_attack_queens, fix_pawn_placement):
    left_queen_pos, right_queen_pos, top_queen_pos, down_queen_pos =  create_four_side_list_compre(fix_attack_queens, fix_pawn_placement)
    queen_four_sides = [left_queen_pos, right_queen_pos, top_queen_pos, down_queen_pos]
    return queen_four_sides


# Get minimal distance beetween queen and pawn in each side
@pytest.fixture()
def fix_min_distance_side(fix_create_four_sides_compre):
    four_sides = fix_create_four_sides_compre
    left_side_queens = four_sides[0]
    rigth_side_queens = four_sides[1]
    top_side_queens = four_sides[2]
    down_side_queens = four_sides[3]
    print("\nleft queens", left_side_queens)
    print("\nrigth queens", rigth_side_queens)
    print("\ntop queens", top_side_queens)
    print("\ndown queens", down_side_queens)

    min_left = min_distance(left_side_queens)
    min_rigth = min_distance(rigth_side_queens)
    min_top = min_distance(top_side_queens)
    min_down = min_distance(down_side_queens)

    # min_values = [min_left, min_rigth, min_top, min_down]
    return min_left, min_rigth, min_top, min_down



# Create list with queens which can direct attack a pawn (from four sides)
@pytest.fixture()
def fix_create_win_queen(fix_attack_queens, fix_min_distance_side, fix_pawn_placement):
    min_left, min_rigth, min_top, min_down = fix_min_distance_side
    print("left min", min_left)
    print("rigth min", min_rigth)
    print("top min", min_top)
    print("down min", min_down)
    win_queen_list = create_win_queen(fix_attack_queens, min_left, min_rigth, min_top, min_down, fix_pawn_placement)
    return win_queen_list

# Create final list with queen which can attact a pawn
@pytest.fixture()
def fix_create_final_list(fix_attack_queens):
    final_list = create_final_list(fix_attack_queens)
    return final_list

# ________________________________Fixtures to ex3
# Remove pawn |P| from test board 
@pytest.fixture()
def fix_remove_current_pawn():
    updated_board = remove_current_pawn(test_board)
    return updated_board


# Remove user Queen |H| from test board 
@pytest.fixture()
def fix_remove_userQueen(fix_attack_queens):
    r_queen_row = fix_attack_queens[0][0]
    r_queen_col = fix_attack_queens[0][1]
    print("row userQueen", r_queen_row)
    print("col userQueen", r_queen_col)
    updated_board = remove_userQueen(r_queen_row, r_queen_col)
    return updated_board