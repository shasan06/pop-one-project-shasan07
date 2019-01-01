# The Three Musketeers Game

# In all methods,
#   A 'location' is a two-tuple of integers, each in the range 0 to 4.
#        The first integer is the row number, the second is the column number.
#   A 'direction' is one of the strings "up", "down", "left", or "right".
#   A 'board' is a list of 5 lists, each containing 5 strings: "M", "R", or "-".
#        "M" = Musketeer, "R" = Cardinal Richleau's man, "-" = empty.
#        Each list of 5 strings is a "row"
#   A 'player' is one of the strings "M" or "R" (or sometimes "-").
#
# For brevity, Cardinal Richleau's men are referred to as "enemy".
# 'pass' is a no-nothing Python statement. Replace it with actual code.
import random
def create_board():
	global board
	"""Creates the initial Three Musketeers board and makes it globally
	available (That is, it doesn't have to be passed around as a
	parameter.) 'M' represents a Musketeer, 'R' represents one of
	Cardinal Richleau's men, and '-' denotes an empty space."""
	m = 'M'
	r = 'R'
	board =	[	[r, r, r, r, m],
				[r, r, r, r, r],
				[r, r, m, r, r],
				[r, r, r, r, r],
				[m, r, r, r, r] ] 

def set_board(new_board):
	"""Replaces the global board with new_board."""
	global board
	for i in range(0,5):
		for j in range(0,5):
			board[i][j] = new_board[i][j]

def get_board():
	"""Just returns the board. Possibly useful for unit tests."""
	return board

def string_to_location(s):
	try:
		if not (s[0] in ('ABCDE')  and s[1] in '12345'):
			raise ValueError
		else:
			return (ord(s[0])-ord('A'),ord(s[1])-ord('1'))
		
	except ValueError:
		print("ValueError: string out of range - " +s)
		raise

	"""Given a two-character string (such as 'A5'), returns the designated
	location as a 2-tuple (such as (0, 4)).
	The function should raise ValueError exception if the input
	is outside of the correct range (between 'A' and 'E' for s[0] and
	between '1' and '5' for s[1]
	"""
   
def location_to_string(loc):
	try:
		if loc[0] in range(0,5) and loc[1] in range(0,5) :
			return chr(ord('A')+loc[0])+ chr(ord('1') +loc[1])
		else:
			raise ValueError
            
	except ValueError:
		print ("ValueError: location out of range")
		raise
		
def at(location):
	"""Returns the contents of the board at the given location.
	You can assume that input will always be in correct range."""
	return board [location[0]][location[1]]

def all_locations():
	"""Returns a list of all 25 locations on the board."""
	return [(i,j) for j in range(5) for i in range(5)]

def adjacent_location(location, direction):
	"""Return the location next to the given one, in the given direction.
	Does not check if the location returned is legal on a 5x5 board.
	You can assume that input will always be in correct range."""
   
	if (direction == 'up'):
		return (location[0]-1,location[1])
	if (direction == 'down'):
		return (location[0]+1,location[1])
	if (direction == 'left'):
		return (location[0],location[1]-1)
	if (direction == 'right'):
		return (location[0],location[1]+1)
		
def is_legal_move_by_musketeer(location, direction):
	"""Tests if the Musketeer at the location can move in the direction.
	You can assume that input will always be in correct range. Raises
	ValueError exception if at(location) is not 'M'"""
	try:
		if at((location[0],location[1]))=='M':
			if is_within_board(location,direction):
				if direction == 'left':
					return at((location[0],location[1]-1))=='R'
				elif direction == 'right':
					return at((location[0],location[1]+1))=='R'
				elif direction == 'up':
					return at((location[0]-1,location[1]))=='R'
				elif direction == 'down':
					return at((location[0]+1,location[1]))=='R'
				else:
					return False
		else:
			raise ValueError
	except ValueError as ve:
		print ("ValueError: Not M")
		raise
	
def is_legal_move_by_enemy(location, direction):
	"""Tests if the enemy at the location can move in the direction.
	You can assume that input will always be in correct range. Raises
	ValueError exception if at(location) is not 'R'"""
	try:
		if at((location[0],location[1]))=='R':
			if(is_within_board(location,direction)):
				if direction   == 'right': 
					return at((location[0],location[1]+1))=='_'
				elif direction == 'left':
					return at((location[0],location[1]-1))=='_'
				elif direction == 'up':
					return at((location[0]-1,location[1]))=='_'
				elif direction == 'down': 
					return at((location[0]+1,location[1]))=='_' 
				else:
					return False
		else:
			raise ValueError
	except ValueError as ve:
		print ("ValueError: Not R")
		raise
		

def is_legal_move(location, direction):
	"""Tests whether it is legal to move the piece at the location
	in the given direction.
	You can assume that input will always be in correct range."""
	if at((location[0],location[1]))=='M':
		return is_legal_move_by_musketeer(location,direction)
	elif at((location[0],location[1]))=='R':
		return is_legal_move_by_enemy(location,direction)
	else:
		return False

def can_move_piece_at(location):
	"""Tests whether the player at the location has at least one move available.
	You can assume that input will always be in correct range.
	You can assume that input will always be in correct range."""
	if len(possible_moves_from(location))==0:
		return False
	else:
		return True

def has_some_legal_move_somewhere(who):
	"""Tests whether a legal move exists for player "who" (which must
	be either 'M' or 'R'). Does not provide any information on where
	the legal move is.
	You can assume that input will always be in correct range."""
	
	try:
		if who in 'MR':
			for i in range(0, len(board)):
				for j in range(0, len(board[i])):
					if board[i][j] == who and can_move_piece_at((i,j)):
						return True
			return False
		else:
			return ValueError
			
	except ValueError:
		print("ValueError: Not M or R")
		raise
	
def possible_moves_from(location):
	"""Returns a list of directions ('left', etc.) in which it is legal
	for the player at location to move. If there is no player at
	location, returns the empty list, [].
	You can assume that input will always be in correct range."""
	list_d=['right','left','down','up']
	possible_moves=[]
	if at((location[0],location[1]))=='_':
		pass
	elif at((location[0],location[1]))=='M':
		for d in list_d:
			if is_legal_move_by_musketeer(location, d):
				possible_moves.append(d)
	elif at((location[0],location[1]))=='R':
		for d in list_d:
			if is_legal_move_by_enemy(location, d):
				possible_moves.append(d)
	return possible_moves
	
def is_legal_location(location):
	"""Tests if the location is legal on a 5x5 board.
	You can assume that input will always be in correct range."""
	
	return location[0] in range(5) and location[1] in range(5)


    
def is_within_board(location, direction):
	"""Tests if the move stays within the boundaries of the board.
	You can assume that input will always be in correct range."""
	
	return is_legal_location(adjacent_location(location,direction))
	
def all_possible_moves_for(player):

	"""Returns every possible move for the player ('M' or 'R') as a list
	(location, direction) tuples.
	You can assume that input will always be in correct range."""
	   
	try:
		if player not in 'MR':
			raise ValueError
		add_possible_moves=[]
		for loc in all_locations():
			if at((loc))==player:
				for dir in possible_moves_from(loc):
					add_possible_moves.append((loc,dir))
		return add_possible_moves
	except ValueError:
		print("ValueError: Not M or R")
		raise
		
def make_move(location, direction):
	"""Moves the piece in location in the indicated direction.	
	Doesn't check if the move is legal. You can assume that input will always
	be in correct range."""
	if is_legal_move(location, direction):
		if at(location)=='M':
			board[adjacent_location(location, direction)[0]][adjacent_location(location, direction)[1]]='M'
			board[location[0]][location[1]]='_'
		elif at(location)=='R': 
			board[adjacent_location(location, direction)[0]][adjacent_location(location, direction)[1]]='R'
			board[location[0]][location[1]]='_'
		
def choose_computer_move(who):
	"""The computer chooses a move for a Musketeer (who = 'M') or an
	enemy (who = 'R') and returns it as the tuple (location, direction),
	where a location is a (row, column) tuple as usual.
	You can assume that input will always be in correct range."""
	
	return random.choice(all_possible_moves_for(who))
	
def is_enemy_win():
	"""Returns True if all 3 Musketeers are in the same row or column."""
	m_list=[]
	for loc in all_locations():
		if at(loc)=='M':
			m_list.append(loc)
	return (m_list[0][0] == m_list[1][0] and m_list[1][0] == m_list[2][0]) or (m_list[0][1] == m_list[1][1] and m_list[1][1] == m_list[2][1])

#---------- Communicating with the user ----------
#----you do not need to modify code below unless you find a bug
#----a bug in it before you move to stage 3

def print_board():
    print("    1  2  3  4  5")
    print("  ---------------")
    ch = "A"
    for i in range(0, 5):
        print(ch, "|", end = " ")
        for j in range(0, 5):
            print(board[i][j] + " ", end = " ")
        print()
        ch = chr(ord(ch) + 1)
    print()

def print_instructions():
    print()
    print("""To make a move, enter the location of the piece you want to move,
and the direction you want it to move. Locations are indicated as a
letter (A, B, C, D, or E) followed by an integer (1, 2, 3, 4, or 5).
Directions are indicated as left, right, up, or down (or simply L, R,
U, or D). For example, to move the Musketeer from the top right-hand
corner to the row below, enter 'A5 left' (without quotes).
For convenience in typing, you may use lowercase letters.""")
    print()

def choose_users_side():
    """Returns 'M' if user is playing Musketeers, 'R' otherwise."""
    user = ""
    while user != 'M' and user != 'R':
        answer = input("Would you like to play Musketeer (M) or enemy (R)? ")
        answer = answer.strip()
        if answer != "":
            user = answer.upper()[0]
    return user

def get_users_move():
    """Gets a legal move from the user, and returns it as a
       (location, direction) tuple."""    
    directions = {'L':'left', 'R':'right', 'U':'up', 'D':'down'}
    move = input("Your move? ").upper().replace(' ', '')
    if (len(move) >= 3
            and move[0] in 'ABCDE'
            and move[1] in '12345'
            and move[2] in 'LRUD'):
        location = string_to_location(move[0:2])
        direction = directions[move[2]]
        if is_legal_move(location, direction):
            return (location, direction)
    print("Illegal move--'" + move + "'")
    return get_users_move()

def move_musketeer(users_side):
    """Gets the Musketeer's move (from either the user or the computer)
       and makes it."""
    if users_side == 'M':
        (location, direction) = get_users_move()
        if at(location) == 'M':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Musketeer", location, direction)
        else:
            print("You can't move there!")
            return move_musketeer(users_side)
    else: # Computer plays Musketeer
        (location, direction) = choose_computer_move('M')         
        make_move(location, direction)
        describe_move("Musketeer", location, direction)
        
def move_enemy(users_side):
    """Gets the enemy's move (from either the user or the computer)
       and makes it."""
    if users_side == 'R':
        (location, direction) = get_users_move()
        if at(location) == 'R':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Enemy", location, direction)
        else:
            print("You can't move there!")
            return move_enemy(users_side)
    else: # Computer plays enemy
        (location, direction) = choose_computer_move('R')         
        make_move(location, direction)
        describe_move("Enemy", location, direction)
        return board

def describe_move(who, location, direction):
    """Prints a sentence describing the given move."""
    new_location = adjacent_location(location, direction)
    print(who, 'moves', direction, 'from',\
          location_to_string(location), 'to',\
          location_to_string(new_location) + ".\n")

def start():
    """Plays the Three Musketeers Game."""
    users_side = choose_users_side()
    board = create_board()
    print_instructions()
    print_board()
    while True:
        if has_some_legal_move_somewhere('M'):
            board = move_musketeer(users_side)
            print_board()
            if is_enemy_win():
                print("Cardinal Richleau's men win!")
                break
        else:
            print("The Musketeers win!")
            break
        if has_some_legal_move_somewhere('R'):
            board = move_enemy(users_side)
            print_board()
        else:
            print("The Musketeers win!")
            break

#---------- Communicating with the user ----------
#----you do not need to modify code below unless you find a bug
#----a bug in it before you move to stage 3

def print_board():
    print("    1  2  3  4  5")
    print("  ---------------")
    ch = "A"
    for i in range(0, 5):
        print(ch, "|", end = " ")
        for j in range(0, 5):
            print(board[i][j] + " ", end = " ")
        print()
        ch = chr(ord(ch) + 1)
    print()

def print_instructions():
    print()
    print("""To make a move, enter the location of the piece you want to move,
and the direction you want it to move. Locations are indicated as a
letter (A, B, C, D, or E) followed by an integer (1, 2, 3, 4, or 5).
Directions are indicated as left, right, up, or down (or simply L, R,
U, or D). For example, to move the Musketeer from the top right-hand
corner to the row below, enter 'A5 left' (without quotes).
For convenience in typing, you may use lowercase letters.""")
    print()

def choose_users_side():
    """Returns 'M' if user is playing Musketeers, 'R' otherwise."""
    user = ""
    while user != 'M' and user != 'R':
        answer = input("Would you like to play Musketeer (M) or enemy (R)? ")
        answer = answer.strip()
        if answer != "":
            user = answer.upper()[0]
    return user

def get_users_move():
    """Gets a legal move from the user, and returns it as a
       (location, direction) tuple."""    
    directions = {'L':'left', 'R':'right', 'U':'up', 'D':'down'}
    move = input("Your move? ").upper().replace(' ', '')
    if (len(move) >= 3
            and move[0] in 'ABCDE'
            and move[1] in '12345'
            and move[2] in 'LRUD'):
        location = string_to_location(move[0:2])
        direction = directions[move[2]]
        if is_legal_move(location, direction):
            return (location, direction)
    print("Illegal move--'" + move + "'")
    return get_users_move()

def move_musketeer(users_side):
    """Gets the Musketeer's move (from either the user or the computer)
       and makes it."""
    if users_side == 'M':
        (location, direction) = get_users_move()
        if at(location) == 'M':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Musketeer", location, direction)
        else:
            print("You can't move there!")
            return move_musketeer(users_side)
    else: # Computer plays Musketeer
        (location, direction) = choose_computer_move('M')         
        make_move(location, direction)
        describe_move("Musketeer", location, direction)
        
def move_enemy(users_side):
    """Gets the enemy's move (from either the user or the computer)
       and makes it."""
    if users_side == 'R':
        (location, direction) = get_users_move()
        if at(location) == 'R':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Enemy", location, direction)
        else:
            print("You can't move there!")
            return move_enemy(users_side)
    else: # Computer plays enemy
        (location, direction) = choose_computer_move('R')         
        make_move(location, direction)
        describe_move("Enemy", location, direction)
        return board

def describe_move(who, location, direction):
    """Prints a sentence describing the given move."""
    new_location = adjacent_location(location, direction)
    print(who, 'moves', direction, 'from',\
          location_to_string(location), 'to',\
          location_to_string(new_location) + ".\n")

def start():
    """Plays the Three Musketeers Game."""
    users_side = choose_users_side()
    board = create_board()
    print_instructions()
    print_board()
    while True:
        if has_some_legal_move_somewhere('M'):
            board = move_musketeer(users_side)
            print_board()
            if is_enemy_win():
                print("Cardinal Richleau's men win!")
                break
        else:
            print("The Musketeers win!")
            break
        if has_some_legal_move_somewhere('R'):
            board = move_enemy(users_side)
            print_board()
        else:
            print("The Musketeers win!")
            break
