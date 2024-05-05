'''''Weryfikacja bicia [4 pkt]
Program powinien odpowiadać na pytania: Czy pionek zostanie zbity
przez któregoś z hetmanów?

Dodakowo: wyświetlić pozycje wszystkich hetmanów, 
którzy mają możliwość zbicia pionka (o ile tacy istnieją).'''


from ex1_create_board import chess_board


# Secoond exercise__________________________________________________
def get_position_queens(board):
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


queen_placements = get_position_queens(chess_board)#list with tuples
# print(f"Queens positions on chess board: {queen_placements}")

def get_position_pawn(board):
     '''Get position of single pawn postion'''

     for row in range(8):
          for col in range(8):
               if board[row][col] == '|P|':
                    row_pawn = row
                    col_pawn = col
                    pawn_tuple = (row_pawn,col_pawn)
                    
     return pawn_tuple

pawn_placement = get_position_pawn(chess_board)#tuple
# print(f"Pawn position on chess board: {pawn_placement}")


def attacked_queen_postion(pawn_placement, queen_placements):
     '''Function to get postion of queens, which can attack a pawn'''

     row_pawn = pawn_placement[0]
     col_pawn = pawn_placement[1]
     queen_list = []
     # Iterate for tuples on list
     for tuple_item in queen_placements:
          row_queen = tuple_item[0]
          col_queen = tuple_item[1]
          # Quenn can attack if it is on the same row, column or diagonal as pawn 
          distance = abs(row_pawn - row_queen) + abs(col_pawn - col_queen)
          if row_pawn == row_queen or  col_pawn == col_queen or  abs(row_pawn - row_queen) == abs(col_pawn - col_queen):
              attack_queen = (row_queen, col_queen, distance)
              queen_list.append(attack_queen)
     return queen_list

attacked_queen_list = attacked_queen_postion(pawn_placement, queen_placements)
#print(f"Attacked queen list - All queens which can attack a pawn: {attacked_queen_list}")

def is_attacked_q(attacked_queen_list):
     '''Function to return True/False for question If pawn is attacked.'''

     if attacked_queen_list != []:
          return True
     else:
          return False
     

def min_distance(side_queen_list):
     '''Function return minimal distance between queen and pawn''' 

     # Set min value
     min = 7

     for tup in side_queen_list: #Przechodzę przez wszystkie elementy
          actual_tup = tup
          dis_actual_tup = actual_tup[2]
          if dis_actual_tup < min:
               min = dis_actual_tup
     return min


# Four list with queens on 4 side of pawn
left_queens = []
rigth_queens = []
top_queens = []
down_queens = []

def create_four_side_list(attacked_queen_list, pawn_placement):
     '''Function create lists with queens on 4 side of pawn.'''

     for tup in attacked_queen_list:
          curr_tup = tup
          # Left -- Queen on left side of pawn, the same row as pawn
          if curr_tup[1] < pawn_placement[1]:#col
               left_queens.append(curr_tup)
          # Rigth --  Queen on rigth side of pawn, the same row as pawn
          elif curr_tup[1] > pawn_placement[1]:#col
               rigth_queens.append(curr_tup)
          # Top
          elif curr_tup[0] < pawn_placement[0]:#row
               top_queens.append(curr_tup)
          # Down
          elif curr_tup[0] > pawn_placement[0]:#row
               down_queens.append(curr_tup)


# List with queen which can direct attack
win_queen = []

def add_queens_list_win_queen(attacked_queen_list, queen_minimum_left, queen_minimum_rigth, queen_minimum_top, queen_minimum_down, pawn_placement):
     '''Function create list with queens which can direct attack a pawn (from four sides)'''

     for tup in attacked_queen_list:
          curr_tup = tup
          # Left
          if curr_tup[1] < pawn_placement[1]:
               if curr_tup[2] == queen_minimum_left:#distance
                    win_queen.append(curr_tup)
          # Right
          if curr_tup[1] > pawn_placement[1]:
               if curr_tup[2] == queen_minimum_rigth:#distance
                    win_queen.append(curr_tup)
          # Top
          if curr_tup[0] < pawn_placement[0]:
               if curr_tup[2] == queen_minimum_top:#distance
                    win_queen.append(curr_tup)
          # Down
          if curr_tup[0] > pawn_placement[0]:
               if curr_tup[2] == queen_minimum_down:#distance
                    win_queen.append(curr_tup)


def create_closest_queen_list(attacked_queen_list):
     '''Function return list with queen which can attact a pawn'''

     if len(attacked_queen_list) == 0:
          print("attacked queen list is empty")
          final_list = []
     elif len(attacked_queen_list) ==   1:
          print("attacked queen list has one value")
          final_list = attacked_queen_list
     else:
          print("attacked queen list a lot of values")
          print("We have to check which queen is closest to pawn.\n")

          # Create Four side list
          create_four_side_list(attacked_queen_list, pawn_placement)
          # print("Left Queens:", left_queens)
          # print("Right Queens:", rigth_queens)
          # print("Top Queens:", top_queens)
          # print("Down Queens:", down_queens)

          # Get min distance on each side
          queen_minimum_left = min_distance(left_queens)
          queen_minimum_rigth = min_distance(rigth_queens)
          queen_minimum_top = min_distance(top_queens)
          queen_minimum_down = min_distance(down_queens)

          # print("Min left distance ", queen_minimum_left)
          # print("Min rigth distance ", queen_minimum_rigth)
          # print("Min top distance " , queen_minimum_top)
          # print("Min down distance", queen_minimum_down)
          
          # Add direct queens to winning list
          add_queens_list_win_queen(attacked_queen_list, queen_minimum_left, queen_minimum_rigth, queen_minimum_top, queen_minimum_down, pawn_placement)
          final_list = win_queen

     return final_list

my_answer = is_attacked_q(attacked_queen_list)
# print(f"\nPawn can be attacked? : {my_answer}")

queen_final_list = create_closest_queen_list(attacked_queen_list)
# print(f"Queen which can direct attack a pawn: {queen_final_list}")





