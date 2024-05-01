import pytest
from ex1_create_board import create_empty_board, place_pawn, place_queen, display_board

#_Info
# grupowanie testów za pomocą mark
# to disable warnings from pytest about markers-> register markers in pytest.ini
# pytest -v –exitfirst - przeprowadzanie testów do failed
# pytest -m 'placement' - puszczanie testów oznaczonych mark
# pytest -v -k ”a1” - puszczanie testów o określonej nazwie
# pytest -v –-maxfail=2 - określenie max ilości failów
# pytest -v –s - żeby wyprintować coś podczas testu
# @pytest.mark.parametrize("test_input",[1,2,3,4]) - określenie setów danych do testowania
#fixtures – robią setup dla innych testów lub robią clean po przeprowadzonych testach
    #• connection to db
    #• open files
#fixtures można zapisać w conftest.py – wtedy dostępne dla całego modułu

#___________________________Scenariusze co będziemy testować
# na planszy miało się pokazać n królowych - sprawdzam czy tyle się pojawiło
# na planszy miał pojawić sie randomowo 1 pionek  - sprawdzam czy się pojawił

# @pytest.mark.placement 
# @pytest.mark.parametrize("test_input",[1,2,3,4])
# def test_place_pawn(test_input):
#     print("ulala")
#     assert test_input>0

# def test_place_queen():
#     assert 5+5 == 11, 'failed test intentionally'

# @pytest.mark.check
# def test_check_figures(init_game_board):
#     pawn_position = init_game_board[0]
#     print(f"Pawn position: {pawn_position}")
#     assert pawn_position == (5,1)

# def test_getItem(setup_list):
#     print(setup_list[0])
#     assert setup_list[0] == "Ala"



@pytest.fixture()
def empty_board():
    print("\nHere we got our empty chess board - we are in fixture")
    empty_board = create_empty_board()
    place_pawn(empty_board)
    place_queen(empty_board)
    display_board(empty_board)
    return empty_board

# @pytest.fixture()
# def show_board():
#     print("\nHere we display chess board - we are in fixture")
#     display_board(empty_board)



def test_one_pawn(empty_board):

    for row in range(8):
          for col in range(8):
               if empty_board[row][col] == '|P|':
                   is_pawn = "Yes"
    assert is_pawn == "Yes"

def test_n_queens(empty_board):
    count_queens = 0
    for row in range(8):
          for col in range(8):
               if empty_board[row][col] == '|H|':
                count_queens += 1
    print(count_queens)
    assert count_queens < 6