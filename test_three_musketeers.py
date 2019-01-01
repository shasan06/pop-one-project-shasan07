import pytest
from three_musketeers import *

left = 'left'
right = 'right'
up = 'up'
down = 'down'
m = 'M'
r = 'R'
_ = '_'

board1 =  [ [_, _, _, m, _],
            [_, _, r, m, _],
            [_, r, m, r, _],
            [_, r, _, _, _],
            [_, _, _, r, _] ]

board2 =  [ [_, m, _, r, _],
            [_, _, r, m, _],
            [m, r, _, r, _],
            [_, r, _, r, _],
            [_, _, r, r, _] ]
			
board3 =  [ [r, r, r, r, m],
            [r, r, r, r, r],
            [r, r, m, r, r],
            [r, r, r, r, r],
            [m, r, r, r, r] ]
			
board4 =  [ [_, r, _, m, _],
            [_, r, _, _, _],
            [r, _, m, _, _],
            [_, r, _, _, _],
            [m, _, _, _, _] ]	
			
board5 =  [ [_, r, _, m, _],
            [_, r, _, _, _],
            [r, _, _, m, _],
            [_, r, _, _, _],
            [r, _, _, m, _] ]
			
board6 =  [ [_, r, _, r, _],
            [_, r, _, _, _],
            [r, _, m, m, m],
            [_, r, _, _, _],
            [r, _, _, r, _] ]			

			
def test_create_board():
	create_board()
	assert at((0,0)) == 'R'
	assert at((0,4)) == 'M'
	assert at((1,2)) == 'R'
	assert at((2,2)) == 'M'
    #eventually add at least two more test cases

def test_set_board():
	set_board(board1)
	assert at((0,2)) == '_'
	assert at((1,3)) == 'M'
	assert at((3,1)) == 'R'     
	set_board(board2)
	assert at((0,0)) == '_'
	assert at((1,3)) == 'M'
	assert at((3,1)) == 'R'    
    #eventually add some board2 and at least 3 tests with it

def test_get_board():
	set_board(board1)
	assert board1[0][2] == '_'
	assert board1[1][3] == 'M'
	assert board1[3][1] == 'R'  
	#eventually add at least one more test with another board

def test_string_to_location():
	with pytest.raises(ValueError):
		string_to_location('X3')
		string_to_location('W9')
	assert string_to_location('A4') == (0,3)
	assert string_to_location('E1') == (4,0)
	assert string_to_location('C3') == (2,2)
	
    #eventually add at least one more exception test and two more
    #test with correct inputs

def test_location_to_string():
	with pytest.raises(ValueError):
		location_to_string((6,9))
		#???
	assert location_to_string((3,4)) == 'D5'
	assert location_to_string((0,3)) == 'A4'
	assert location_to_string((4,0)) == 'E1'
	assert location_to_string((2,2)) == 'C3'


def test_at():
	for i in range(0,5):
		for j in range(0,5):
			assert at((i,j)) in 'MR_'
	set_board(board1)
	assert at((0,2)) == '_'
	assert at((1,3)) == 'M'
	assert at((3,1)) == 'R' 	

def test_all_locations():
	set_board(board3)
	all_loc=all_locations()
	assert len(all_loc)==25
	for loc in all_loc:
		assert loc[0] in range(5) and loc[1] in range(5)
		
	
def test_adjacent_location():

	assert adjacent_location((2,4),'left') == (2,3)
	assert adjacent_location((0,3),'down') == (1,3)
	assert adjacent_location((1,4),'up') == (0,4)
	assert adjacent_location((4,1),'right') == (4,2)
 
	
def test_is_legal_move_by_musketeer():
	set_board(board1)
	assert is_legal_move_by_musketeer((1,3),'left')==True
	assert is_legal_move_by_musketeer((2,2),'right')==True	
	assert is_legal_move_by_musketeer((2,2),'up')==True
	assert is_legal_move_by_musketeer((0,3),'right')==False
	assert is_legal_move_by_musketeer((1,3),'down')==True
	#???exception
def test_is_legal_move_by_enemy():
	set_board(board1)
	assert is_legal_move_by_enemy((1,2),'right')==False
	assert is_legal_move_by_enemy((1,2),'left')==True
	assert is_legal_move_by_enemy((2,3),'up')==False
	assert is_legal_move_by_enemy((2,1),'up')==True
	assert is_legal_move_by_enemy((1,2),'down')==False
	
	

def test_is_legal_move():
	set_board(board1)
	assert is_legal_move((0,3),'right')==False
	assert is_legal_move((1,2),'left')==True
	assert is_legal_move((0,3),'down')==False
	assert is_legal_move((2,3),'right')==True
	assert is_legal_move((1,3),'down')==True

def test_can_move_piece_at():
	set_board(board1)
	assert can_move_piece_at((0,0))==False
	assert can_move_piece_at((1,2))==True
	assert can_move_piece_at((0,3))==False
	assert can_move_piece_at((2,3))==True
	assert can_move_piece_at((1,3))==True

def test_has_some_legal_move_somewhere():
	set_board(board1)
	assert has_some_legal_move_somewhere('M') == True
	assert has_some_legal_move_somewhere('R') == True
	set_board(board4)
	assert has_some_legal_move_somewhere('M') == False
	assert has_some_legal_move_somewhere('R') == True
    # Eventually put at least three additional tests here
    # with at least one additional board

def test_possible_moves_from():
	set_board(board1)
	assert 'up' in possible_moves_from((4,3))
	assert 'down' in possible_moves_from((3,1))
	assert 'right' in possible_moves_from((2,3))	
	assert 'left' in possible_moves_from((1,2))
	assert 'up' not in possible_moves_from((1,3))
	assert 'down' not in possible_moves_from((2,1))
	assert 'right' not in possible_moves_from((0,3))
	assert 'left' not in possible_moves_from((2,3))
    

def test_is_legal_location():
	set_board(board1)
	assert is_legal_location((1,3))==True
	assert is_legal_location((0,3))==True
	assert is_legal_location((2,2))==True
	assert is_legal_location((3,0))==True
	assert is_legal_location((1,5))==False
	assert is_legal_location((6,3))==False
	assert is_legal_location((2,7))==False
	assert is_legal_location((8,0))==False

def test_is_within_board():
	set_board(board1)
	assert is_within_board((2,2),'right')==True
	assert is_within_board((3,1),'left')==True
	assert is_within_board((1,2),'up')==True
	assert is_within_board((3,2),'down')==True
	assert is_within_board((4,4),'right')==False
	assert is_within_board((2,0),'left')==False
	assert is_within_board((0,0),'up')==False
	assert is_within_board((4,4),'down')==False
	
def test_all_possible_moves_for():
	set_board(board1)
	assert len(all_possible_moves_for('M'))==5
	assert len(all_possible_moves_for('R'))==12
	print(all_possible_moves_for('M'))
	set_board(board2)
	assert len(all_possible_moves_for('M'))==4
	assert len(all_possible_moves_for('R'))==17
	set_board(board3)
	assert len(all_possible_moves_for('M'))==8
	assert len(all_possible_moves_for('R'))==0
	set_board(board4)
	assert len(all_possible_moves_for('M'))==0
	assert len(all_possible_moves_for('R'))==12
	set_board(board5)
	assert len(all_possible_moves_for('M'))==0
	assert len(all_possible_moves_for('R'))==14
	set_board(board6)
	assert len(all_possible_moves_for('M'))==0
	assert len(all_possible_moves_for('R'))==20
	
	
	
	
	
	
	
def test_make_move():
	set_board(board1)
	make_move((1,2),'left')
	assert at((1,2)) == '_'
	assert at((1,1)) == 'R'
	make_move((2,2),'right')
	assert at((2,2)) == '_'
	assert at((2,3)) == 'M'
	make_move((3,1),'down')
	assert at((3,1)) == '_'
	assert at((4,1)) == 'R'

    
	
def test_choose_computer_move():
	d_list = ['up','down','left','right']
	if len(all_possible_moves_for('M'))>0:
		assert is_legal_location(choose_computer_move('M')[0])
		assert choose_computer_move('M')[1] in d_list
	if len(all_possible_moves_for('R'))>0:
		assert is_legal_location(choose_computer_move('R')[0])
		assert choose_computer_move('R')[1] in d_list
	
def test_is_enemy_win():
	set_board(board1)
	assert is_enemy_win() == False
	
	set_board(board2)
	assert is_enemy_win() == False
	
	set_board(board3)
	assert is_enemy_win() == False
	
	set_board(board4)
	assert is_enemy_win() == False
	
	set_board(board5)
	assert is_enemy_win() == True
	
	set_board(board6)
	assert is_enemy_win() == True


