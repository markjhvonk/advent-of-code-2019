import math

input = open("input.txt", "r")

fuel = 0

readInput = input.readlines()
# for module in readInput:
#     mass = int(module.rstrip())
#     moduleFuel = math.trunc(mass/3) - 2
#     fuel += moduleFuel
#     print(moduleFuel)

totalFuel = 33583

def recursive_fuel(fuel):
    global totalFuel
    # Base case: 1! = 1
    if fuel <= 0:
        print('stahp')
        return str(totalFuel)

    # Recursive case: n! = n * (n-1)!
    else:
        newFuel = math.trunc(fuel/3) - 2
        totalFuel += newFuel
        print(newFuel)
        return recursive_fuel(newFuel)


recursive_fuel(33583)

print('total fuel: ' + str(totalFuel))
# print('total fuel: ' + str(fuel))