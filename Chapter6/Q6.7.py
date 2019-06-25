from random import *

def runNfamilies(n: int) -> float:
    boys = 0
    girls = 0

    for i in range(n):
        genders = runOneFamily()
        boys += genders[0]
        girls += genders[1]

    return girls / (girls + boys)

def runOneFamily():
    girls = 0
    boys = 0
    while girls == 0:
        if randint(0, 1) == 0:
            girls += 1
        else:
            boys += 1

    return [boys, girls]


print(runNfamilies(10))
