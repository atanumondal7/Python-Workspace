import random

pc = [0 for _ in range(5)]
mc = [0 for _ in range(5)]
win = [0 for _ in range(5)]

def turn(matrix):
    
    q = 0;
    print("")
    print("Your turn!")
    print("")
    while q != 1:
        
        p = input("")
        i = int(p[0])
        j = int(p[1])
        
        if i <= 2  and j <= 2 and len(p) == 2:
            if(matrix[i][j] == '-'):
                q = 1
            else:
                print("")
                print("Location is already occupied!")
                print("Try again!")
                print("")
                show(matrix)
                
        elif i > 2 or j > 2:
            print("")
            print("Out of bounds of matrix!")
            print("Try again")
            print("")
            show(matrix)
            
        else:
            print("")
            print("Unsupported Input!")
            print("Try again")
            print("")
            show(matrix)
            
    return i,j

def checkso(matrix):
    if matrix[0][0] == 'O' and matrix[1][0] == 'O' and matrix[2][0] == 'O':
        return True
    if matrix[0][1] == 'O' and matrix[1][1] == 'O' and matrix[2][1] == 'O':
        return True
    if matrix[0][2] == 'O' and matrix[1][2] == 'O' and matrix[2][2] == 'O':
        return True
    if matrix[0][0] == 'O' and matrix[0][1] == 'O' and matrix[0][2] == 'O':
        return True
    if matrix[1][0] == 'O' and matrix[1][1] == 'O' and matrix[1][2] == 'O':
        return True
    if matrix[2][0] == 'O' and matrix[2][1] == 'O' and matrix[2][2] == 'O':
        return True
    if matrix[0][0] == 'O' and matrix[1][1] == 'O' and matrix[2][2] == 'O':
        return True
    if matrix[2][0] == 'O' and matrix[1][1] == 'O' and matrix[0][2] == 'O':
        return True
    else:
        return False

def checksx(matrix):
    if matrix[0][0] == 'X' and matrix[1][0] == 'X' and matrix[2][0] == 'X':
        return True
    if matrix[0][1] == 'X' and matrix[1][1] == 'X' and matrix[2][1] == 'X':
        return True
    if matrix[0][2] == 'X' and matrix[1][2] == 'X' and matrix[2][2] == 'X':
        return True
    if matrix[0][0] == 'X' and matrix[0][1] == 'X' and matrix[0][2] == 'X':
        return True
    if matrix[1][0] == 'X' and matrix[1][1] == 'X' and matrix[1][2] == 'X':
        return True
    if matrix[2][0] == 'X' and matrix[2][1] == 'X' and matrix[2][2] == 'X':
        return True
    if matrix[0][0] == 'X' and matrix[1][1] == 'X' and matrix[2][2] == 'X':
        return True
    if matrix[2][0] == 'X' and matrix[1][1] == 'X' and matrix[0][2] == 'X':
        return True
    else:
        return False
    
def show(matrix):
    print("")
    print("")
    print(f"{matrix[0][0]}  {matrix[0][1]}  {matrix[0][2]}")
    print(f"{matrix[1][0]}  {matrix[1][1]}  {matrix[1][2]}")
    print(f"{matrix[2][0]}  {matrix[2][1]}  {matrix[2][2]}")
    print("")
    print("")

def playagain(pscore, mscore, gamenumber):
    
    if gamenumber == 5:
        games(pscore, mscore, gamenumber)
    
    print("")
    print("Do you wish to play again?")
    print("[Y for Yes, N for No]")
    pa = input("")
    
    
    if pa == 'Y':
        games(pscore, mscore, gamenumber)
        
    elif pa == 'N':
        print("")
        print("Thank you for playing! Hope you enjoyed our game!")
        exit(0)
        
    else:
        print("Invalid Input")
        playagain(pscore, mscore, gamenumber)
        
def scoreboard(k, pscore, mscore, gamenumber):
    
    if k == 1:
        pscore += 1
    elif k == 2:
        mscore += 1
    else:
        pass
        
    print("")
    print("Scoreboard:-")
    print(f"Player: {pscore}")
    print(f"Computer: {mscore}")
    print("")
    
    playagain(pscore, mscore, gamenumber)
    
def checker(matrix, p, itr, pscore, mscore, gamenumber):
    
    if p == 'O':
        if checkso(matrix):
            print("")
            print("Player Wins!")
            win[gamenumber-1] = 1
            scoreboard(1, pscore, mscore, gamenumber)
        if checksx(matrix):
            print("")
            print("Computer Wins!")
            win[gamenumber-1] = 0
            scoreboard(2, pscore, mscore, gamenumber)
        if itr == 5:
            print("")
            print("Draw!")
            win[gamenumber-1] = 2
            scoreboard(0, pscore, mscore, gamenumber)
            
    elif p == 'X':
        if checkso(matrix):
            print("")
            print("Computer Wins!")
            win[gamenumber-1] = 0
            scoreboard(2, pscore, mscore, gamenumber)
        if checksx(matrix):
            print("")
            print("Player Wins!")
            win[gamenumber-1] = 1
            scoreboard(1, pscore, mscore, gamenumber)
        if itr == 5:
            print("")
            print("Draw!")
            win[gamenumber-1] = 2
            scoreboard(0, pscore, mscore, gamenumber)
            
    else:
        pass
    
def pomx(matrix, it, pscore, mscore, gamenumber):
    a,b = turn(matrix)
    matrix[a][b] = 'O'
    
    show(matrix)
    checker(matrix, 'O', it, pscore, mscore, gamenumber)
    
    a1 = random.randint(0,2)
    b1 = random.randint(0,2)
    
    while matrix[a1][b1] != '-':
        a1 = random.randint(0,2)
        b1 = random.randint(0,2)
        
    matrix[a1][b1] = 'X'
    
    print("Computer's turn:")
    print("")
    show(matrix)
    checker(matrix, 'O', it, pscore, mscore, gamenumber)
    
    
def pxmo(matrix, it, pscore, mscore, gamenumber):
    
    a1 = random.randint(0,2)
    b1 = random.randint(0,2)
    
    while matrix[a1][b1] != '-':
        a1 = random.randint(0,2)
        b1 = random.randint(0,2)
        
    matrix[a1][b1] = 'O'
    
    print("Computer's turn:")
    print("")
    show(matrix)
    checker(matrix, 'X', it, pscore, mscore, gamenumber)
    
    a,b = turn(matrix)
    matrix[a][b] = 'X'
    
    show(matrix)
    checker(matrix, 'X', it, pscore, mscore, gamenumber)
        
            
def pchoice(matrix, pscore, mscore, gamenumber):
    
    print(f"Game {gamenumber}")
    print("")
    choice = input("Enter your choice: (X or O)\n")
    print("")
    k = 0
    
    if choice == 'O':
        
        pc[gamenumber-1] = 'O'
        mc[gamenumber-1] = 'X' 
        while k <= 9:
            k+=1
            pomx(matrix, k, pscore, mscore, gamenumber)
            
    elif choice == 'X':
        pc[gamenumber-1] = 'X'
        mc[gamenumber-1] = 'O' 
        while k <= 9:
            k+=1
            pxmo(matrix, k, pscore, mscore, gamenumber)
                       
    else:
        print("Invalid Choice")
        pchoice(matrix, pscore, mscore, gamenumber)
        
def initialize(matrix, pscore, mscore, gamenumber):
    
    gamenumber += 1
    
    for i in range(3):
        for j in range(3):
            matrix[i][j] = '-'
    pchoice(matrix, pscore, mscore, gamenumber)
    
def winner(n):
    if n == 0:
        print("Winner: Computer")
    if n == 1:
        print("Winner: Player")
    if n == 2:
        print("Winner: None [Draw]")
    else:
        pass

def gameshow(n, matrix):
    print(f"Game {n}:")
    print("")
    print(f"Player: {pc[n-1]}")
    print(f"Computer: {mc[n-1]}")
    print("")
    print("Game: ")
    show(matrix)
    print("")
    winner(win[n-1])
    print("")

def games(pscore, mscore, gamenumber):
    
    if gamenumber == 0:
        initialize(matrix1, pscore, mscore, gamenumber)
    if gamenumber == 1:
        initialize(matrix2, pscore, mscore, gamenumber)
    if gamenumber == 2:
        initialize(matrix3, pscore, mscore, gamenumber)
    if gamenumber == 3:
        initialize(matrix4, pscore, mscore, gamenumber)
    if gamenumber == 4:
        initialize(matrix5, pscore, mscore, gamenumber)
        
    if gamenumber == 5:
        print("")
        print("Welcome to Game Review:")
        print("")
        gameshow(1, matrix1)
        gameshow(2, matrix2)
        gameshow(3, matrix3)
        gameshow(4, matrix4)
        gameshow(5, matrix5)
        exit(0)

def score():
    
    pscore = 0
    mscore = 0
    gamenumber = 0
    
    games(pscore, mscore, gamenumber)
    
matrix1 = [[0 for _ in range(3)] for _ in range(3)]
matrix2 = [[0 for _ in range(3)] for _ in range(3)]
matrix3 = [[0 for _ in range(3)] for _ in range(3)]
matrix4 = [[0 for _ in range(3)] for _ in range(3)]
matrix5 = [[0 for _ in range(3)] for _ in range(3)]

score()

