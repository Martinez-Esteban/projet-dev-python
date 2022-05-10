import socket
from os import system, name
from solo import check_win


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux
    else:
        _ = system('clear')


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 1111))
except:
    clear()
    print("/!\ Server not found ! \n")
    exit()

# init game
clear()
grid = [[" - ", " - ", " - "], [" - ", " - ", " - "], [" - ", " - ", " - "]]
turn = True
player = "X"
count = 0
for line in grid:
    print(''.join(line))


# main game loop
while count < 9:
    if(turn):
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
        grid[l][c] = " " + player + " "
        move = str(l) + str(c)
        s.send(move.encode())
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

s.send("END".encode())


# s.send(username.encode())
# r = s.recv(2048)
