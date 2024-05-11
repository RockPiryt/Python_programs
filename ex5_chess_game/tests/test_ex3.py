from ex1_create_board import display_board


def test_remove_current_pawn(fix_remove_current_pawn):
    print("\nupdated chess board without pawn")
    updated_board = fix_remove_current_pawn
    display_board(updated_board)
    assert updated_board
    # assert count_pawn == 0

def test_remove_userQueen(fix_remove_userQueen):
    print("\nupdated chess board withut userQueen")
    updated_board = fix_remove_userQueen
    display_board(updated_board)
    assert updated_board

# def test_menu():
#     pass