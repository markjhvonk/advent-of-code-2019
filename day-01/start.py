import math

input = open("input.txt", "r")

fuel = 0

readInput = input.readlines()
for module in readInput:
    mass = int(module.rstrip())
    moduleFuel = math.trunc(mass/3) - 2
    fuel += moduleFuel
    print(moduleFuel)

print('total fuel: ' + str(fuel))