import pytest
from ex1_create_board import create_empty_board, place_pawn, place_queen, display_board
from ex2_move_linear import get_position_pawn, get_position_queens

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

# Get location of pawn
@pytest.fixture()
def pawn_placement(chess_board):
    pawn_location = get_position_pawn(chess_board)
    print("\nPawn Placement:", pawn_location)
    return pawn_location

# Get locations of queens
@pytest.fixture()
def queen_placements(chess_board):
    queen_locations = get_position_pawn(chess_board)
    print("\nQueen Placement:", queen_locations)
    return queen_locations