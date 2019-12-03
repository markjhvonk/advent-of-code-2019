import math

input = open("input.txt", "r")

totalFuel = 0

def fuelForFuel(inputFuel):
    global totalFuel

    newFuel = math.trunc(inputFuel/3) - 2
    
    if newFuel <= 0:
        return

    else:
        totalFuel += newFuel
        print(newFuel)
        return fuelForFuel(newFuel)

readInput = input.readlines()

for module in readInput:
    mass = int(module.rstrip())
    fuelForFuel(mass)

print('total fuel: ' + str(totalFuel))