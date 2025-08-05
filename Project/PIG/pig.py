import random as r

def roll():
    min_val = 1
    max_val = 6
    roll = r.randint(min_val,max_val)
    return roll

while True :
    players = input("Enter the number of players 2-4 - ")
    
    if players.isdigit():
        players = int(players)
        if 2<= players <= 4 :
            break
        else:
            print("Must be between 2-4 players")
    else:
        print("Must be a digit from 2 - 4 ")    
            
print(players)