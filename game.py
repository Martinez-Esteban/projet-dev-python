import os
clear = lambda: os.system('clear')

clear()
grid = [[" - "," - "," - "],[" - "," - "," - "],[" - "," - "," - "]]
turn = True
player = "X"
count = 0
for line in grid:
    print(''.join(line))

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

while count < 9:
    if(turn == True):
        player = "X"
    else:
        player = "O"
    print("\nTour de : ", player)
    print("\nLigne (entre 1 et 3) :")
    l = int(input())-1
    print("Colonne (entre 1 et 3) :")
    c = int(input())-1
    clear()
    if(l <= 3 and c <= 3 and grid[l][c] == " - "):
        if(player == "X"):
            grid[l][c] = " X "
        else:
            grid[l][c] = " O "
        for line in grid:
            print(''.join(line))
        turn = not turn
        count += 1
        if(check_win()):
            print("\nVictoire de : ", player)
            break
    else:
        for line in grid:
            print(''.join(line))
        print("wrong input")
        
if(not check_win()):
    print("\nMatch nul")