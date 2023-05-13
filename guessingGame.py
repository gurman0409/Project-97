import random
print("NUMBER GUESSING GAME!!!")
number = random.randint(1, 9)
chances = 0
print("Guess a number (between 1 and 9):")

while chances < 5:
    guess = int(input("ENTER YOUR GUESS:- "))

    if guess == number:
        print("CONGRATULATIONS YOU WON!!!")
        break

    elif guess < number:
        print("Your guess was too low: Guess a number higher than", guess)

    else:
        print("Your guess was too high: Guess a number lower than", guess)

    chances += 1

if not chances < 5:
    print("YOU LOSE!!! , THE NUMBER IS", number)

    