""" Batle ship game
Created by: Krzysiek Zminkowski a.k.a Cichy

Classic Batle ship game. The goal is to sink all the ships.
There are one 4 mast ship, two 3 mast ships, three 2 mast ships
and four 1 mast ships.
At the begining the player has 5 tries. For every hit the player
gets +1 try. For every miss the player looses one try.

Have fun."""

import random

def creat_board():
    """creates an empty board"""
    board = {}
    for i in range(1,11):
        board[i] = list("0" * 10)
    return board

def print_board(board):
    """Displays the board to the player in a easy-to-read way"""
    print("A B C D E F G H I J")
    for key in board:
        print(str(" ".join(board[key])) + " :" +str(key))
        
def four_mast_ship(board):
    """Creates a 4 mats ship"""
    #chooses one of the ship versions
    ver = random.randint(0,8)
    if ver == 0:
        #seeds the first mast
        row = random.randint(1,8)
        col = random.randint(0,8)
        #checks if the choosen row and comumn is free and if not it's looking for a free place
        while board[row][col] != "0" or board[row][col+1] != "0" or board[row+1][col] != "0" or board[row+1][col+1] != "0":
            row = random.randint(1,8)
            col = random.randint(0,8)
        #pleaces the masts of the ship
        board[row][col] = "4"
        board[row][col+1] = "4"
        board[row+1][col] = "4"
        board[row+1][col+1] = "4"
    elif ver == 1:
        row = random.randint(1,8)
        col = random.randint(0,7)
        while board[row][col] != "0" or board[row][col+1] != "0" or board[row][col+2] != "0" or board[row+1][col] != "0":
            row = random.randint(1,8)
            col = random.randint(0,7)
        board[row][col] = "4"
        board[row][col+1] = "4"
        board[row][col+2] = "4"
        board[row+1][col] = "4"
    elif ver == 2:
        row = random.randint(1,8)
        col = random.randint(0,7)
        while board[row][col] != "0" or board[row+1][col] != "0" or board[row+1][col+1] != "0" or board[row+1][col+2] != "0":
            row = random.randint(1,8)
            col = random.randint(0,7)
        board[row][col] = "4"
        board[row+1][col] = "4"
        board[row+1][col+1] = "4"
        board[row+1][col+2] = "4"
    elif ver == 3:
        row = random.randint(1,8)
        col = random.randint(0,7)
        while board[row][col] != "0" or board[row][col+1] != "0" or board[row][col+2] != "0" or board[row+1][col+1] != "0":
            row = random.randint(1,8)
            col = random.randint(0,7)
        board[row][col] = "4"
        board[row][col+1] = "4"
        board[row][col+2] = "4"
        board[row+1][col+1] = "4"
    elif ver == 4:
        row = random.randint(1,8)
        col = random.randint(0,7)
        while board[row][col] != "0" or board[row][col+1] != "0" or board[row][col+2] != "0" or board[row+1][col+2] != "0":
            row = random.randint(1,8)
            col = random.randint(0,7)
        board[row][col] = "4"
        board[row][col+1] = "4"
        board[row][col+2] = "4"
        board[row+1][col+2] = "4"
    elif ver == 5:
        row = random.randint(2,9)
        col = random.randint(0,7)
        while board[row][col] != "0" or board[row][col+1] != "0" or board[row][col+2] != "0" or board[row-1][col+1] != "0":
            row = random.randint(2,9)
            col = random.randint(0,7)
        board[row][col] = "4"
        board[row][col+1] = "4"
        board[row][col+2] = "4"
        board[row-1][col+1] = "4"
    elif ver == 6:
        row = random.randint(1,7)
        col = random.randint(0,9)
        while board[row][col] != "0" or board[row+1][col] != "0" or board[row+2][col] != "0" or board[row+3][col] != "0":
            row = random.randint(1,7)
            col = random.randint(0,9)
        board[row][col] = "4"
        board[row+1][col] = "4"
        board[row+2][col] = "4"
        board[row+3][col] = "4"
    elif ver == 7:
        row = random.randint(1,10)
        col = random.randint(0,6)
        while board[row][col] != "0" or board[row][col+1] != "0" or board[row][col+2] != "0" or board[row][col+3] != "0":
            row = random.randint(1,7)
            col = random.randint(0,9)
        board[row][col] = "4"
        board[row][col+1] = "4"
        board[row][col+2] = "4"
        board[row][col+3] = "4"    
    else:
        row = random.randint(2,9)
        col = random.randint(0,7)
        while board[row][col] != "0" or board[row][col+1] != "0" or board[row][col+2] != "0" or board[row-1][col+2] != "0":
            row = random.randint(2,9)
            col = random.randint(0,7)
        board[row][col] = "4"
        board[row][col+1] = "4"
        board[row][col+2] = "4"
        board[row-1][col+2] = "4"
        
    return board
    
def three_mast_ship(board):
    """Creates a 3 mast ship. 
    The procedure of creation a 3 mast ship is the same as of creating a 4 mast ship, so there are no additional comments in this function"""
    ver = random.randint(0,5)
    if ver == 0:
        row = random.randint(1,8)
        col = random.randint(0,9)
        while board[row][col] != "0" or board[row+1][col] != "0" or board[row+2][col] != "0":
            row = random.randint(1,8)
            col = random.randint(0,9)
        board[row][col] = "3"
        board[row+1][col] = "3"
        board[row+2][col] = "3"
    elif ver == 1:
        row = random.randint(1,10)
        col = random.randint(0,7)
        while board[row][col] != "0" or board[row][col+1] != "0" or board[row][col+2] != "0":
            row = random.randint(1,10)
            col = random.randint(0,7)
        board[row][col] = "3"
        board[row][col+1] = "3"
        board[row][col+2] = "3"
    elif ver == 2:
        row = random.randint(1,9)
        col = random.randint(0,8)
        while board[row][col] != "0" or board[row][col+1] != "0" or board[row+1][col] != "0":
            row = random.randint(1,9)
            col = random.randint(0,8)
        board[row][col] = "3"
        board[row][col+1] = "3"
        board[row+1][col] = "3"
    elif ver == 3:
        row = random.randint(1,9)
        col = random.randint(0,8)
        while board[row][col] != "0" or board[row+1][col+1] != "0" or board[row+1][col] != "0":
            row = random.randint(1,9)
            col = random.randint(0,8)
        board[row][col] = "3"
        board[row+1][col+1] = "3"
        board[row+1][col] = "3"
    elif ver == 4:
        row = random.randint(1,9)
        col = random.randint(0,8)
        while board[row][col] != "0" or board[row][col+1] != "0" or board[row+1][col+1] != "0":
            row = random.randint(1,9)
            col = random.randint(0,8)
        board[row][col] = "3"
        board[row][col+1] = "3"
        board[row+1][col+1] = "3"
    else:
        row = random.randint(2,10)
        col = random.randint(0,8)
        while board[row][col] != "0" or board[row][col+1] != "0" or board[row-1][col+1] != "0":
            row = random.randint(1,9)
            col = random.randint(0,8)
        board[row][col] = "3"
        board[row][col+1] = "3"
        board[row-1][col+1] = "3"
    
    return board

def two_mast_ship(board):
    """Creates a 2 mast ship. 
    The procedure of creation a 2 mast ship is the same as of creating a 4 mast ship, so there are no additional comments in this function"""
    ver = random.randint(0,1)
    if ver == 0:
        row = random.randint(1,9)
        col = random.randint(0,9)
        while board[row][col] != "0" or board[row+1][col] != "0":
            row = random.randint(1,9)
            col = random.randint(0,9)
        board[row][col] = "2"
        board[row+1][col] = "2"
    elif ver == 1:
        row = random.randint(1,10)
        col = random.randint(0,8)
        while board[row][col] != "0" or board[row][col+1] != "0":
            row = random.randint(1,10)
            col = random.randint(0,8)
        board[row][col] = "2"
        board[row][col+1] = "2"

    return board

def one_mast_ship(board):
    """Creates one mast ship"""
    row = random.randint(1,10)
    col = random.randint(0,9)
    while board[row][col] != "0":
        row = random.randint(1,10)
        col = random.randint(0,9)
    board[row][col] = "1"
    
    return board
    
def shooting(board, disp_board):
    dict_col={"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9}
    hit = 0
    shot = input("Take a shot (first row, then column): " )
    row_shot = int(shot[:-1])
    if row_shot > 10:
        print("There is no row {}".format(row_shot))
        return(disp_board, hit, 0, shot)
    col_shot = shot[-1].upper()
    if col_shot in dict_col:
        col_shot_ind = dict_col[col_shot]
    else:
        print("There is no column {}".format(col_shot))
        return(disp_board, hit, 0, shot)
    if board[row_shot][col_shot_ind] in "1234":
        print("It's a hit! Go on!")
        disp_board[row_shot][col_shot_ind] = board[row_shot][col_shot_ind]
        hit = 1
    else:
        print("You missed.")
        disp_board[row_shot][col_shot_ind] = "X"
        hit = 0
    
    return (disp_board, hit, board[row_shot][col_shot_ind], shot)
    
def buffor(board):
    for key in board:
        for i in range(10):
            if board[key][i] in "1234":
                try:
                    if board[key-1][i] == "0":
                        board[key-1][i] = "-"
                except:
                    pass
                try:
                    if board[key-1][i-1] == "0":
                        board[key-1][i-1] = "-"
                except:
                    pass
                try:
                    if board[key-1][i+1] == "0":
                        board[key-1][i+1] = "-"
                except:
                    pass
                try:
                    if board[key][i+1] == "0":
                        board[key][i+1] = "-"
                except:
                    pass
                try:
                    if board[key+1][i+1] == "0":
                        board[key+1][i+1] = "-"
                except:
                    pass
                try:
                    if board[key+1][i] == "0":
                        board[key+1][i] = "-"
                except:
                    pass
                try:
                    if board[key+1][i-1] == "0":
                        board[key+1][i-1] = "-"
                except:
                    pass
                try:
                    if board[key][i-1] == "0":
                        board[key][i-1] = "-"
                except:
                    pass
    return board

def main():    
    #cretaing the game board and placeing shops:
    board = creat_board()
    disp_board = creat_board()
    board = four_mast_ship(board)
    board = buffor(board)
    board = three_mast_ship(board)
    board = buffor(board)
    board = three_mast_ship(board)
    board = buffor(board)
    board = two_mast_ship(board)
    board = buffor(board)
    board = two_mast_ship(board)
    board = buffor(board)
    board = two_mast_ship(board)
    board = buffor(board)
    board = one_mast_ship(board)
    board = buffor(board)
    board = one_mast_ship(board)
    board = buffor(board)
    board = one_mast_ship(board)
    board = buffor(board)
    board = one_mast_ship(board)
    #print_board(board)#this line is just for tests
    print_board(disp_board)
    #variables for tries and game stats
    tries = 5
    used_tries = 0
    hits = 0
    ships = []
    shots = []
    #loop in which the player tries to hit a ship
    while tries > 0:
        disp_board, hit, mast, shot = shooting(board, disp_board)
        shot = shot[:-1] + shot[-1].upper()
        #displaying board:
        print_board(disp_board)
        #checking if the shot is a hit:
        if hit == 1 and shot not in shots:
            tries +=1
            hits += hit
            ships.append(mast)
            shots.append(shot)
        elif shot in shots:
            tries = tries
            print("You allready shot here earlier")
        else:
            tries -= 1
        print("You have {} tries left".format(tries))
        #print("List of shots on target: " + str(shots))#this line is just for tests
        #print("Curren shot: " + shot)#this line is just for tests
        #print("List of mast hited: " + str(ships)) #this line is just for tests
        #countinh stats:
        used_tries += 1
        #checking if palyer has won if yes displays message and game stats:
        if len(ships) == 20:
            print("\nCongratulations You won!")
            print("\nGame stats:\nYou uesd {0} tries\nYou had {1} hits\nYour hit ratio is {2:.1f}%".format(used_tries, hits, hits/used_tries*100))
            break
        #if there are no tries left displays game over message and game stats:
        if tries == 0:
            print("\nGame over!\nThanks for playing!\nSee you soon!")
            print("\nGame stats:\nYou uesd {0} tries\nYou had {1} hits\nYour hit ratio is {2:.1f}%".format(used_tries, hits, hits/used_tries*100))
            
main()