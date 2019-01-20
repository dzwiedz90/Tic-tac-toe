import os
import tictactoeMainMenu

a1 = ' '
a2 = ' '
a3 = ' '
b1 = ' '
b2 = ' '
b3 = ' '
c1 = ' '
c2 = ' '
c3 = ' '
players = tictactoeMainMenu.player()
print(players)

os.system('cls')
print('##############################################################################################')
print('##################################        TIC TAC TOE       ##################################')
print('##############################################################################################')
print(' ')
print('               Pole gry                      Tablica współrzędnych')
print(' ')

print('               |     |               |              |     |			')
print('            '+a1+'  |  '+a2+'  |  '+a3+'            |           a1 |  a2 |  a3		')
print('          _ _ _|_ _ _|_ _ _          |         _ _ _|_ _ _|_ _ _		')
print('               |     |               |              |     |			')
print('            '+b1+'  |  '+b2+'  |  '+b3+'            |           b1 |  b2 |  b3		')
print('          _ _ _|_ _ _|_ _ _          |         _ _ _|_ _ _|_ _ _		')
print('               |     |               |              |     |			')
print('            '+c1+'  |  '+c2+'  |  '+c3+'            |           c1 |  c2 |  c3		')
print('               |     |               |              |     |			')
print('')
print('')
#input('Player '+tictactoeMainMenu.players[0]+' enter a number: ')