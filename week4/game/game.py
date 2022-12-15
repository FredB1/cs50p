from random import randint
while True:
    try:
        level = int(input("Level: "))
        guess = randint(1,level)
    except:
        pass
    else:
        break
while True:
    try:
        attempt = int(input("Guess: "))
        if attempt < 0:
            raise
        if attempt < guess:
            print("Too small!")
            raise
        if attempt > guess:
            print("Too large!")
            raise
    except:
        pass
    else:
        break
print("Just right!")