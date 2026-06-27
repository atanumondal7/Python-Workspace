import random
ag = 1
a = []
min1 = 0
ind = 0
while ag != 0:
    print("Difficulty levels - [1-10, 1-100, 1-1000]")
    n = int(input("Enter the highest number: "))
    choice = random.randint(1,n)
    print("I have chosen a random number!")
    print("Try to guess it!")
    attempts = 0
    guess = 0
    


    while guess != choice:
        guess = int(input(""))
        attempts += 1
        
        if guess > choice:
            print("Too high, try lower!")
        elif guess < choice:
            print("Too low, try higher!")
        else:
            print(f"Fantastic work! You have guessed the number in {attempts} attempts!\n")
    
    a.append(attempts)
    
    a1 = sorted(list(set(a)))
    k = len(a)
    
    print("")
    print("===================================")
    print("===================================")
    print(f"Score(s) of the last {k} game(s):")
    print("")
    for i in range (k):
        if a[i] == a1[0]:
            print(f"Game {i+1}: {a[i]}  [1st]")
        elif k>1 and a[i] == a1[1]:
            print(f"Game {i+1}: {a[i]}  [2nd]")
        elif k>2 and a[i] == a1[2]:
            print(f"Game {i+1}: {a[i]}  [3rd]")
        else:
            print(f"Game {i+1}: {a[i]}")
    print("===================================")
    print("===================================")
    print("")
    
    guess = 0
    print("")
    ag = int(input("Press 1 to play again or press 0 to terminate the session!\n"))

        
