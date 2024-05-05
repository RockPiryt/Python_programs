import pytest

from ex2_move_linear import (get_position_queens, get_position_pawn, 
                             attacked_queen_postion, is_attacked_q, min_distance,
                             create_four_side_list, add_queens_list_win_queen, create_closest_queen_list)


# Test Scenarios
# 1. Test to check if we get postions of all queens on board 
# 2. Test to check if on chess board is max 5 queens 


# Tests Data
pawn_placement = (4,4)
queen_placements_test = [(1,4), (2,4), (3,4), (6,4), (5,4), (4,5),(4,6),(4,2), (4,1)]
attack_queen_test= [(1,4,3), (2,4,2), (3,4,1), (6,4,2), (5,4,1), (4,5,1),(4,6,2),(4,2,2), (4,1,3)]

# print("Queen placements", queen_placements)
# print("Pawn placement", pawn_placement)


# 1. Test to check if we get postions of all queens on board 
def test_get_position_queens(chess_board):
    '''Get positions of all generated queens'''
    
    count_queens = 0
    for row in range(8):
        for col in range(8):
            if chess_board[row][col] == '|H|':
                count_queens += 1
    print(f"On chess board are {count_queens} queens")
    queen_placements = get_position_queens(chess_board)
    print("Queen placements:", queen_placements)
    
    assert len(queen_placements) == count_queens
    
    

def test_get_position_pawn(chess_board):
    '''Get position of single pawn postion'''
    count_pawn = 0
    for row in range(8):
        for col in range(8):
            if chess_board[row][col] == '|P|':
                count_pawn += 1
    pawn_list= []           
    pawn_placement = get_position_pawn(chess_board)
    pawn_list.append(pawn_placement)
    print("Pawn placement:", pawn_placement)
    assert len(pawn_list) == count_pawn
    
@pytest.mark.parametrize("attack_queen", attack_queen_test)
def test_attacked_queen_postion(attack_queen):
    '''Function to get postion of queens, which can attack a pawn'''
    # attacked_queen_list = attacked_queen_postion(pawn_placement, queen_placements)
    assert attack_queen in queen_placements

# def test_is_attacked_q(attacked_queen_list):
#     '''Function to return True/False for question If pawn is attacked.'''
#     pass

# def test_min_distance(side_queen_list):
#     '''Function return minimal distance between queen and pawn''' 
#     pass

# def test_create_four_side_list(attacked_queen_list, pawn_placement):
#     '''Function create lists with queens on 4 side of pawn.'''
#     pass

# def test_add_queens_list_win_queen(attacked_queen_list, queen_minimum_left, queen_minimum_rigth, queen_minimum_top, queen_minimum_down, pawn_placement):
#     '''Function create list with queens which can direct attack a pawn (from four sides)'''
#     pass

# def test_create_closest_queen_list(attacked_queen_list):
#     '''Function return list with queen which can attact a pawn'''
#     pass

