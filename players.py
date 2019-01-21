import os



def playerName():
	os.system('cls')
	print('##############################################################################################')
	print('##################################        TIC TAC TOE       ##################################')
	print('##############################################################################################')
	print(' ')
	players = ['','']
	players[0] = input('Player 1 what is your name?: ')
	players[1] = input('Player 2 what is your name?: ')
	return players