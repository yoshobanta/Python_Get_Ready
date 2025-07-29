import random
# from collections import defaultdict
# res = defaultdict(int)

# print(random.randrange(-1,11))   # it have start stop similarly to range . here it will start form 0 and exclude 11

# print(random.randint(-1,11))     # it will include 11 . also it required 2 positional argument unlike randrange which required only one.

# for _ in range(10):
#     res[random.randint(1,10)] += 1

# print(res)

## Now the crux is we have to guess the number until then the loop will iterate.

number = random.randint(-1,10)
attempts = 0

while True:
    user_guess = int(input("enter a number"))
    attempts += 1
    if user_guess == number:
        print("Your Guess is right")
        print(f"The number of attempts required to guess the right answer ifs - {attempts}")
        break
    elif user_guess > number:
        print("The enter number is greater than the answer")
    elif user_guess < number:   
        print("The enter number is less than the answer")
    

