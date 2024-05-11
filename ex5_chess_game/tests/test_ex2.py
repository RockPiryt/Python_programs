
# Test to check if we get position of max 5 test queens
def test_get_position_queens(fix_queen_locations_test):
    '''Get positions of all generated queens'''

    print(f"\nTest Queen is on position: {fix_queen_locations_test}")
    
    assert len(fix_queen_locations_test) <= 5
    
        
# Test to check if we get position of 1 pawn
def test_get_position_pawn(fix_pawn_placement):
    '''Get position of single pawn'''

    pawn_location = []           
    pawn_location.append(fix_pawn_placement)
    print(f"\n Test Pawn placement: {fix_pawn_placement}")
    assert len(pawn_location) == 1
    
#  Test to check if there is max 5 queens which can attack a pawn
def test_attacked_queen_postion(fix_attack_queens):
    '''Function to get postion of queens, which can attack a pawn'''
     
    print(f"Possible attacked queens list: {fix_attack_queens}")

    assert len(fix_attack_queens) <= 5 


# def test_is_attacked_q(fix_attack_queens):
#     '''Function to return True/False for question If pawn is attacked.'''
#     answer = is_attacked_q(fix_attack_queens)
#     if len(fix_attack_queens) != 0:
#         can_attack = True
#     assert 

# Test to check if min distance is between 1-7
def test_min_distance(fix_min_distance):
    '''Function return minimal distance between queen and pawn''' 
    
    distances_list = list(range(1,8))
    print("\nFix min distance: ",fix_min_distance)

    assert fix_min_distance in distances_list 


# Test to check if 4 list were created
def test_create_four_side_list(fix_create_four_sides_compre):
    '''Function create lists with queens on 4 side of pawn.'''

    four_lists = fix_create_four_sides_compre
    print("\n",four_lists)
    print("\nLeft queens ", four_lists[0])
    print("\nRight queens ", four_lists[1])
    print("\nTop queens ", four_lists[2])
    print("\nDown queens ", four_lists[3])

    assert len(fix_create_four_sides_compre) == 4

# Test to check if win queen list was created
def test_create_win_queen(fix_create_win_queen):
    '''Function create list with queens which can direct attack a pawn (from four sides)'''
    print("Win queen list: ",fix_create_win_queen)
    if fix_create_win_queen != None:
        win_list_created = True
    assert win_list_created

def test_create_final_list(fix_create_final_list):
    '''Function return list with queen which can attact a pawn'''
    print("final list: ", fix_create_final_list)
    if fix_create_final_list != None:
        final_list_created = True
    assert final_list_created 

    
