'''
This is a TIC _ TAC _ TOE
This is my 1st game 😍😍😍👍 
I just love python  👍

'''

from IPython.display import clear_output
import random

def display_board(board):
	print('\n'*100)
	print('|'+board[7]+'|'+board[8]+'|'+board[9]+'|')
	print('|'+board[4]+'|'+board[5]+'|'+board[6]+'|')
	print('|'+board[1]+'|'+board[2]+'|'+board[3]+'|')


#take the player 1 and Player 2 input 

def player_input():
	marker=' '
	
	while marker !='X' and marker !='O':
		marker = input('Enter Your Choise , X or O --> ').upper()
	if marker =='X':
		return('X','O')
	else:
		return ('O','X')
	#player 2 will get the opposite value of player 1
	
#define the function that will assign a value to the board position between 1-9

def place_marker(board, marker, position):
	
	board[position] = marker
	
#now check for the marker has own the game or not 

def win_check(board,mark):
	
	return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
	(board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
	(board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
	(board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
	(board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
	(board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
	(board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
	(board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal#now chose the player who will play first

def choose_first():
	flip=random.randint(0,1)
	
	if flip==1:
		return 'player1'
	else :
		return 'player2'

#now check the space in the board is free or not 
def space_check(board, position):
	return board[position]==' '

#Now check the board is full or not 

def full_board_check(board):
	
	for  x in range(1,10):
		if space_check(board,x):
			return False
	
	return True

#now take the next input from the user ..

def player_choice(board):
	position=0
	
	while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position) :
		position = int(input('Enter a value between 1-9 --> '))
	return position

#Ask the player that they want to play again or nor 

def replay():
	choice=''
	input('Do you want to play again , "YES" or "NO" -->  ').upper()
	if choice=='YES' :
		return True
	else :
		return False
	
#Here is thr final part of the game , where we will use the while loop and the function to run the game 

while True:
	
	#Set the game up here
	
	the_board = [' ']*10
	player1_marker,player2_marker=player_input()
	#assign the Turn too the player from the merthod
	turn = choose_first()
	print(turn+' will play the game ')
	#Now ask the player that he/she want to play or not 
	play_game=input('Are you ready to play , Y or N --> ').upper()
	
	if play_game == 'Y':
		game_on = True
	else :
		game_on= False
	
	#execution depends on the value of game_on (True or Flase)
	
	while game_on:
		
		if turn == 'player1':
			
			#now this is player1 turn 
			
			display_board(the_board)
			#chose the position
			position = player_choice(the_board)
			#place the marker to the postion
			place_marker(the_board, player1_marker, position)
			#check the Win 
			if win_check(the_board, player1_marker):
				display_board(the_board)
				print('Player 1 WAN 👍👍👍 !!')
				game_on = False
			else :
				if full_board_check(the_board):
					display_board(the_board)
					print('There is a TIE 😟😕🥺 ')
					break
				else :
					turn = 'player2'
		
		#player2 turn 
		else :
			display_board(the_board)
			#chose the position
			position = player_choice(the_board)
			#place the marker to the postion
			place_marker(the_board, player2_marker, position)
			#check the Win 
			if win_check(the_board, player2_marker):
				display_board(the_board)
				print('Player 2 WAN 👍👍👍  !!')
				game_on = False
			else :
				if full_board_check(the_board):
					display_board(the_board)
					print('There is a TIE 😟😕🥺  ')
					break
				else :
					turn = 'player1'
			
	if not replay():
		break

			
					
			
			
			
			
			
	
	
	
	
		
	
	