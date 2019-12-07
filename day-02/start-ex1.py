program = open("input.txt", "r")

intcode = list(map(int, program.read().replace('\n', '').split(",")))

section = 12
prevSection = section - 4

# opCode = intcode[:section]

# for code in opCode:
#     print(code)

def runCode(opCode):
    # print(opCode)
    global section
    global prevSection

    calc = 0

    if (opCode[0] == 99):
        print('break')
        return
    else:
        if (opCode[0] == 1):
            calc = opCode[opCode[1]] + opCode[opCode[2]]
        elif (opCode[0] == 2):
            calc = opCode[opCode[1]] * opCode[opCode[2]]
        print(calc)
        section += 4
        print(section)
        runCode(intcode[prevSection:section])

# runCode(intcode[prevSection:section])
print(intcode[prevSection:section])
