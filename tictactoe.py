# global variables

board = ["Z"] + ([" "] * 9)
mark = "X"
game_on = True

def display():
    
    print('\n'*100)
    print('     |   |')
    print('   ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('     |   |')
    print('  -----------')
    print('     |   |')
    print('   ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('     |   |')
    print('  -----------')
    print('     |   |')
    print('   ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('     |   |')
    print('\n')

def winner():
	return ((board[7] == mark and board[8] == mark and board[9] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[7] == mark and board[4] == mark and board[1] == mark) or 
    (board[8] == mark and board[5] == mark and board[2] == mark) or 
    (board[9] == mark and board[6] == mark and board[3] == mark) or 
    (board[7] == mark and board[5] == mark and board[3] == mark) or 
    (board[9] == mark and board[5] == mark and board[1] == mark)) 

def full_board():
	return " " not in board

def clear_board(board):
	return ["Z"] + ([" "] * 9)

def switch_mark(mark):
	if mark == "X":
		return "O"
	else:
		return "X"

def place_mark():

	space_available = False
	choice = " "

	while choice.isdigit() == False or int(choice) not in range(1,10) or not space_available:

		display()
		choice = input(f'Choose an empty position (1-9) to place an {mark}')
		if choice.isdigit() and int(choice) in range(1,10):

			position = int(choice)
			if board[position] == " ":

				space_available = True
				board[position] = mark
				display()


while game_on:
	
	place_mark()
	
	if full_board():
		choice = " "
		while choice not in ["y", "n"]:
			choice = input("It's a draw. Play again? (y/n)")
		if choice == "y":
			board = clear_board(board)
		else:
			game_on = False

	if winner():
		choice = " "
		while choice not in ["y", "n"]:
			choice = input(f"{mark} is the winner! Play again? (y/n)")
		if choice == "y":
			board = clear_board(board)
		else:
			game_on = False

	mark = switch_mark(mark)
