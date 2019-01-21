import os
import players

#przerobić na słownik
f = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
#    a1  a2  a3  b1  b2  b3  c1  c2  c3 
#	 0	 1	 2	 3	 4	 5	 6	 7	 8

players = players.playerName()
print('Hello '+players[0]+', you will be X,  hello '+players[1]+', you will be O!')
input('Press enter to continue...')
gameOver = False

def hasWon():
	if(((f[0]=='X') and (f[3]=='X') and (f[6]=='X')) or ((f[1]=='X') and (f[4]=='X') and (f[7]=='X')) or ((f[2]=='X') and (f[5]=='X') and (f[8]=='X'))):
		gameOver = True
		print('Game over! '+players[0]+' won!')
	elif((f[0]=='X' and f[1]=='X' and f[2]=='X') or (f[3]=='X' and f[4]=='X' and f[5]=='X') or (f[6]=='X' and f[7]=='X' and f[8]=='X')):
		gameOver = True
		print('Game over! '+players[0]+' won!')
	elif((f[0]=='X' and f[4]=='X' and f[8]=='X') or (f[2]=='X' and f[4]=='X' and f[6]=='X')):
		gameOver = True
		print('Game over! '+players[0]+' won!')
	elif((f[0]=='O' and f[3]=='O' and f[6]=='O') or (f[1]=='O' and f[4]=='O' and f[7]=='O') or (f[2]=='O' and f[5]=='O' and f[8]=='O')):
		gameOver = True
		print('Game over! '+players[1]+' won!')
	elif((f[0]=='O' and f[1]=='O' and f[2]=='O') or (f[3]=='O' and f[4]=='O' and f[5]=='O') or (f[6]=='O' and f[7]=='O' and f[8]=='O')):
		gameOver = True
		print('Game over! '+players[1]+' won!')
	elif((f[0]=='O' and f[4]=='O' and f[8]=='O') or (f[2]=='O' and f[4]=='O' and f[6]=='O')):
		gameOver = True
		print('Game over! '+players[1]+' won!')
		
	
def fillField():
	playerNumber = 0
	while gameOver == False:
		hasWon()
		gameField()
		playerNumber = playerNumber
		playerMark = ''
		if playerNumber == 0: playerMark = 'X'
		elif playerNumber == 1: playerMark = 'O'
		choose = input(players[playerNumber]+': '+playerMark+', your move! Which field?: ')
		f[int(choose)] = playerMark
		playerNumber += 1
		if playerNumber>1: playerNumber = 0
		print(f)

def gameField():
	os.system('cls')
	print('##############################################################################################')
	print('##################################        TIC TAC TOE       ##################################')
	print('##############################################################################################')
	print(' ')
	print('               Pole gry                      Tablica współrzędnych')
	print(' ')

	print('               |     |               |              |     |			')
	print('            '+f[0]+'  |  '+f[1]+'  |  '+f[2]+'            |            0 |   1 |   2		')
	print('          _ _ _|_ _ _|_ _ _          |         _ _ _|_ _ _|_ _ _		')
	print('               |     |               |              |     |			')
	print('            '+f[3]+'  |  '+f[4]+'  |  '+f[5]+'            |            3 |   4 |   5		')
	print('          _ _ _|_ _ _|_ _ _          |         _ _ _|_ _ _|_ _ _		')
	print('               |     |               |              |     |			')
	print('            '+f[6]+'  |  '+f[7]+'  |  '+f[8]+'            |            6 |   7 |   8		')
	print('               |     |               |              |     |			')
	print('')
	print('')
	
fillField()