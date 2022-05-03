import os
from random import randint

clear = lambda: os.system('clear')

# init game
clear()
grid = [[" - "," - "," - "],[" - "," - "," - "],[" - "," - "," - "]]
turn = True
player = "X"
count = 0
for line in grid:
    print(''.join(line))
     
# function to check if someone won   
def check_win():
    for line in grid:
        if(line[0] == line[1] == line[2] and line[0] != " - "):
            return True
    for line in grid:
        if(line[0] == line[1] == line[2] and line[0] != " - "):
            return True
    if(grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != " - "):
        return True
    if(grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != " - "):
        return True
    return False
    
if randint(0,1) == 0:
    turn = False
else:
    turn = True
    
# main game loop
while count < 9:
    print("\nVous : X")
    if(turn):
        player = "X"
        print("\nLigne (entre 1 et 3) :")
        l = int(input())-1
        print("Colonne (entre 1 et 3) :")
        c = int(input())-1
        clear()
        if(l <= 3 and c <= 3 and grid[l][c] == " - "):
            grid[l][c] = " " + player + " "
            for line in grid:
                print(''.join(line))
            turn = not turn
            count += 1
            if(check_win()):
                print("\nVictoire de : ", player + "\n")
                break
        else:
            for line in grid:
                print(''.join(line))
            print("wrong input")
    else:
        player = "O"
        l = randint(0,2)
        c = randint(0,2)
        clear()
        if grid[l][c] == " - ":
            grid[l][c] = " " + player + " "
            for line in grid:
                print(''.join(line))
            turn = not turn
            count += 1
            if(check_win()):
                print("\nVictoire de : ", player + "\n")
                break
        
if(not check_win()):
    print("\nMatch nul")