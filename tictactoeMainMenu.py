import os
import sys



def main():
	os.system('cls')
	print('##############################################################################################')
	print('##################################                          ##################################')
	print('##################################        TIC TAC TOE       ##################################')
	print('##################################                          ##################################')
	print('##############################################################################################')
	print(' ')
	print('ver. 1.0')
	print('(C) by dzwiedz90\nWszystkie prawa zastrzeżone')
	print(' ')

	input('Wciśnij enter, aby kontynuować...')
	os.system('cls')

	choose = 0
	while choose == 0:
		print('1. Nowa gra')
		print('2. Wyjdź')	
		choose = input('Wybierz tryb i naciśnij enter: ')
		os.system('cls')
		if choose == '1':
			break
		elif choose == '2':
			sys.exit(0)

	os.system('cls')
	print('##############################################################################################')
	print('##################################        TIC TAC TOE       ##################################')
	print('##############################################################################################')
	print(' ')
	global players = ['a','b']
	players[0] = input('Player 1 what is your name?: ')
	players[1] = input('Player 2 what is your name?: ')

def playerName()
	return players
	
main()