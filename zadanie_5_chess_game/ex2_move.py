'''''Weryfikacja bicia [4 pkt]
Program powinien odpowiadać na pytania: Czy pionek zostanie zbity
przez któregoś z hetmanów?

Dodakowo: wyświetlić pozycje wszystkich hetmanów, 
którzy mają możliwość zbicia pionka (o ile tacy istnieją).'''


from ex1_create_board import chess_board

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

def position_pawn(board):
     '''Get single pawn postion'''

     for row in range(8):
          for col in range(8):
               if board[row][col] == '|P|':
                    row_pawn = row
                    col_pawn = col
                    
     return (row_pawn, col_pawn)

pawn_placement = position_pawn(chess_board)#tuple
print(f"Pawn position on chess board: {pawn_placement}")


# Row and col of pawn
row_pawn = pawn_placement[0]
col_pawn = pawn_placement[1]

# #tests___________
# row_pawn = 5
# col_pawn = 0

def is_attacked_by_queen(row_pawn, col_pawn, row_queen, col_queen):
    '''Function to check if queen can attack a pawn'''

    # Queen can attack if it is on the same row, column or diagonal as pawn 
    if (row_pawn == row_queen or  col_pawn == col_queen or  abs(row_pawn - row_queen) == abs(col_pawn - col_queen)):
        return True
    else:
        return False

def attacked_queen_postion(row_pawn, col_pawn, row_queen, col_queen ):
      '''Function to get postion of queens, which can attack a pawn'''

      # Quenn can attack if it is on the same row, column or diagonal as pawn 
      distance = abs(row_pawn - row_queen) + abs(col_pawn - col_queen)
      if (row_pawn == row_queen or  col_pawn == col_queen or  abs(row_pawn - row_queen) == abs(col_pawn - col_queen)):
           return (row_queen, col_queen, distance)
    
attacked_queen_list = []
# Iterate for tuples on list
for tuple_item in queen_placements:
      row_queen = tuple_item[0]
      col_queen = tuple_item[1]
      pawn_situation = is_attacked_by_queen(row_pawn, col_pawn, row_queen, col_queen)
      if pawn_situation == True:
        win_queen_position = attacked_queen_postion(row_pawn, col_pawn, row_queen, col_queen)
        attacked_queen_list.append(win_queen_position)

print(f"Postion of allqueens which are on the same row/col/diagonal as pawn: {attacked_queen_list}")

# #tests____________________________________________________      
# attacked_queen_list = [(4, 0, 2), (5, 0, 1), (5, 6, 5)]
# print(f"Postion of allqueens which are on the same row/col/diagonal as pawn: {attacked_queen_list}")

closest_queens_positions = []

def closest_queens(attacked_queen_list):
     '''Function to check if exist other queen on attacked line''' 
     
     for i in range(len(attacked_queen_list)): #list=2 #i= 0 #i=1#i=2
        #   current_tuple = attacked_queen_list[i] 
        #   row_value = current_tuple[0]
        #   col_value = current_tuple[1]
        #   position_q = (row_value, col_value)
        #   closest_queens_positions.append(position_q) 
          
          # Add postion if all col and row in all tuples are diffrent
          for j in range(0, (len(attacked_queen_list)- i-1)): #j=0 #end=2-0 = 2  czyli zrobi 3 razy#j=1 end=2-1=1#j=2 end=2-2
               current_tuple = attacked_queen_list[j] #0 czyli 1 tupla, #j=1 czyli tupla 2, j=0 czyli
               next_tuple = attacked_queen_list[j + 1]

               row_value = current_tuple[0]
               row_value_next = next_tuple[0]

               col_value = current_tuple[1]
               col_value_next = next_tuple[1]

               dist_value = current_tuple[2]
               dist_value_next = next_tuple[2]

               position_q = (row_value, col_value, dist_value)
               print(position_q)
               position_q_next = (row_value_next, col_value_next, dist_value_next)
               print(position_q_next)
        #        if position_q[0] == row_pawn and position_q_next[0] == row_pawn and position_q[2] < position_q_next[2]:
               if (position_q[2] < position_q_next[2] and position_q[0] == position_q_next[0] == row_pawn) or (position_q[2] < position_q_next[2] and position_q[1] == position_q_next[1] == col_pawn):
                        closest_queens_positions.append(position_q)
                        
                        print("First win")
                        # return position_q
               elif (position_q[2] > position_q_next[2] and position_q[0] == position_q_next[0] == row_pawn) or (position_q[2] > position_q_next[2] and position_q[1] == position_q_next[1] == col_pawn):
                        closest_queens_positions.append(position_q_next)
                        print("Second win")
                        # return position_q_next
        #        elif position_q[2] < position_q_next[2] and position_q[1] == position_q_next[1] == col_pawn:
        #                 closest_queens_positions.append(position_q)
        #                 print("EEE")
        #        elif position_q[2] > position_q_next[2] and position_q[1] == position_q_next[1] == col_pawn:
        #                 closest_queens_positions.append(position_q_next)
        #                 print("zzz")
               else:
                  print("CCC")
                #   closest_queens_positions.append(position_q)  
closest_queens(attacked_queen_list)
print(f"Closest queen position:{closest_queens_positions}")

if len(attacked_queen_list) == 1:
     row_value = attacked_queen_list[0][0]
     col_value = attacked_queen_list[0][1]
     position_q = (row_value, col_value)
     closest_queens_positions.append(position_q)

elif  len(attacked_queen_list) > 1:    
        only_win_queens = closest_queens(attacked_queen_list)
print(f"Postion of attacked queens: {closest_queens_positions}")


