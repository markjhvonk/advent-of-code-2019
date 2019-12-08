program = open("input.txt", "r")

intcode = list(map(int, program.read().replace('\n', '').split(",")))

section = 4

def runCode(opCode):
    global intcode
    global section

    calc = 0

    if (opCode[0] == 99):
        print('break')
        print(intcode[0])
        return
    else:
        if (opCode[0] == 1):
            calc = intcode[opCode[1]] + intcode[opCode[2]]
        elif (opCode[0] == 2):
            calc = intcode[opCode[1]] * intcode[opCode[2]]
        
        intcode[opCode[3]] = calc
        section += 4
        prevSection = section -4
        runCode(intcode[prevSection:section])

runCode(intcode[0:section])
