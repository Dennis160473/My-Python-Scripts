import random

Computer = ["Schere", "Stein", "Papier"]


def selectRandom(Computer):
    return random.choice(Computer)


print("The name selected is: ", selectRandom(Computer))
