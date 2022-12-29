


import random
while True:
    print("Welcome to guessing game")
    user_score=0
    print("You Have Three Chances To Guess.")
    a = range(10)
    b = random.choice(a)
    c = int(input("Enter your First Guess:"))
    d = int(input("Enter Your Second Guess:"))
    f = int(input("Enter Your Third Guess:"))
    if c == b:
        print("You won")
        print(b)
        user_score+=1
    elif d == b:
        print("You won")
        print(b)
        user_score+=1
    elif f == b:
        print("You won")
        print(b)
        user_score+=1
    else:
        print("Better Luck Next Time")
        print(b)

    print("Your score:",user_score)



    again=str(input("Have one more try: "))
    if again =="no" or again =="No":
        break

print("Game Over")
print("Thanks for playing")
