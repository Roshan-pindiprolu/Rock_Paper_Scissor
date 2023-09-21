import random
num = random.randrange(1,10)
guess = int(input("What is the number? "))
while num != guess:
    if guess > num:
        print("Too Low")
        guess = int(input("What is the number? "))
    elif guess < num:
        print("Too High")
        guess = int(input("What is the number? "))
if num == guess:
    print("You have guessed it")