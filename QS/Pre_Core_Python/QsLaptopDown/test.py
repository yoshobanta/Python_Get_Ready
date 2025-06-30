
users = [
    {"username": "abc", "password": "abc123"},
    {"username": "xyz", "password": "xyz123"}
]

un = input("enter a username -")
i = 0
while i < len(users):
    if un == users[i]["username"]:
        pw = input("enter a password -")
        if pw == users[i]["password"]:
            print("users logedin")
            break
        else:
            print("wrong password")
            break
    i +=1
else:
    print("wrong username")