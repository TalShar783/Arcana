import random


def rollDice(number, size, modifier=1):
    result = 0 + modifier
    for x in range(number):
        result += random.randrange(1, size)
    return f"{result}"

def chooseElement():
    elementsList = [
        "Fire",
        "Cold",
        "Force",
        "Lightning and Thunder",
        "Radiant",
        "Necrotic and Psychic"
    ]
    return random.choice(elementsList)