# Here we will store our password in a txt file.
# We will ask the user if they want to add a new password or view the password .
# We will also create a master password

from cryptography.fernet import Fernet


master_pwd = input("What is the master password ?")

def view():
       with open("passwords.txt") as f:
        for i in f:
            
            data = i.strip().split()             #For clean and no extra tralling or leading white space .
            # data = i.split()
            print(f"Account name - {data[0].strip()}")
            print(f"Password - {data[2].strip()}")
            print("-------------------------------------------")
        

def add():
    name = input("Account name : ")
    pwd = input("Password : ")
    with open("passwords.txt", "a") as f :
        f.write(f"{name} | {pwd}\n")

while True:
    mode = input("To add password type 'add' To view the password type - 'view' and to quit type - 'q'").lower()
    if mode in ("quit","q"):
        break
    
    if mode in ("view","v"):
        view()
    elif mode in ("add","a"):
        add()
    else:
        print("Type a valid input")
        continue
        