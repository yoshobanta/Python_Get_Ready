# Rock/Paper/Scissors game
import random

user_wins = 0
comp_wins = 0

options = ["rock","paper","scissor"]

while True:
    user_ip = input("Type Rock/Paper or Scissors or Q to quit : ").lower()
    if user_ip ==  "q":
        break             
    # or exit() It will stop the entire execution of the program, But break will just take the control outside of the loop.
    
    if user_ip not in ("rock","paper","scissor"):
        print("Pls Type Rock/Paper or Scissors")
        continue
    
    rand_pick = random.randint(0,2)
    comp_ip = options[rand_pick]
    
    if user_ip == "rock" and comp_ip == "scissor":
        print("User Win")
        user_wins += 1
       
    elif user_ip == "scissor" and comp_ip == "paper":
        print("User Win")
        user_wins += 1
    
    elif user_ip == "paper" and comp_ip == "rock":
        print("User Win")
        user_wins += 1
    
    else:
        print("Comp Wins")
        comp_wins += 1
 
print(f"Score of user - {user_wins} and comp - {comp_wins} ")   
print("Thank You For PLaying")
    
        
    