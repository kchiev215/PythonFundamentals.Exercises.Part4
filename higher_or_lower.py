import random
randomizedNumber = random.randrange(1,10)
while True:
    userGuess = int(input("guess a number from 1-10 "))
    if userGuess > randomizedNumber:
        print("too high. Try again")
    elif userGuess < randomizedNumber:
        print("too low. Try again")
    elif userGuess == randomizedNumber:
        print("ding ding ding. Nice work")
        break

