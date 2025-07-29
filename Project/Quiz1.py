print("Hello Welcome to kon banega Winner (Mere ko paisa wapis de dena)")
play = input("You want to play! yes(y)/no(n)").lower()
count = 0
score = 0
# print(play)
# if play == "yes" and  play != "y":
if play not in ("yes","y"):
    print("Khel le na bhai.Easy game hai maa kasam")
    exit()
else:
    print("Let's Start the game !")
    print("1. What is the Python")
    choice1 = input("a)Programing Language b)Reptile c)AI language d)None \n").lower()
    score += 1
    
    if choice1 in ("programing language","a") :
        print("Correct")
        count +=1
        print(f"Your Score is {count} of {score}")
    else:
        print("Wrong")
        print(f"Your Score is {count} of {score}")
      
    print("2. Capital of Odisha")  
    choice2 = input("a)Rkl b)BBSR c)SBP d)None \n").lower()
    score += 1
    
    if choice2 in ("BBSR","b") :
        print("Correct")
        count +=1
        print(f"Your Score is {count} of {score}")
    else:
        print("Wrong")
        print(f"Your Score is {count} of {score}")
             
    print("3. What does a compiler do?")  
    choice3 = input("A) Translates high-level code into machine code B) Runs the program line by line C) Edits your code D) Compiles data into charts \n").lower()
    score += 1
    
    if choice3 in ("Translates high-level code into machine code","a") :
        print("Correct")
        count +=1
        print(f"Your Score is {count} of {score}")
    else:
        print("Wrong")
        print(f"Your Score is {count} of {score}")
        
        
    print("4. Which of the following is NOT a programming language?")  
    choice4 = input(" A) Python B) Java C) HTML D) Linux \n").lower()
    score += 1
    
    if choice4 in ("HTML","c") :
        print("Correct")
        count +=1
        print(f"Your Score is {count} of {score}")
    else:
        print("Wrong")
        print(f"Your Score is {count} of {score}")
        
    print("5. What is a bug in programming?")  
    choice4 = input(" A) A type of code B) A special keyword C) An error or flaw in the program D) A tool to write code \n").lower()
    score += 1
    
    if choice4 in ("An error or flaw in the program","c") :
        print("Correct")
        count +=1
        print(f"Your Score is {count} of {score}")
    else:
        print("Wrong")
        print(f"Your Score is {count} of {score}")