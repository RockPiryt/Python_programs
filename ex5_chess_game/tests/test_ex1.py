from ex1_create_board import  place_pawn, place_queen

# Test Scenarios
# 1. Test to check if is one pawn on test chess board
# 2. Test to check if on chess board is max 5 queens 


# Test to check if is one pawn on test chess board
def test_one_pawn(empty_board):
    place_pawn(empty_board)
    for row in range(8):
          for col in range(8):
               if empty_board[row][col] == '|P|':
                   is_pawn = "Yes"
    assert is_pawn == "Yes"

# Test to check if on chess board is max 5 queens 
def test_n_queens(empty_board):
    place_queen(empty_board)
    count_queens = 0
    for row in range(8):
          for col in range(8):
               if empty_board[row][col] == '|H|':
                count_queens += 1
    print(f"Current count of queens on chess board: {count_queens}")
    assert count_queens < 6