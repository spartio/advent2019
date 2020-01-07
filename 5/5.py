from imports.imports import readFile


def operate(list):
    i = ifirst = isecond = 0
    while list[i] != 99:
        opcode = (lambda x: x % 100)(list[i])
        first_parameter = (lambda x, n: x // 10 ** n % 10)(list[i], 2)
        second_parameter = (lambda x, n: x // 10 ** n % 10)(list[i], 3)
        try:
            ifirst = list[i + 1] if first_parameter else list[list[i + 1]]
            isecond = list[i + 2] if second_parameter else list[list[i + 2]]
        except IndexError:
            pass

        if opcode == 1 or opcode == 2:
            list[list[i + 3]] = ifirst + isecond if opcode == 1 else ifirst * isecond
            i += 4

        elif opcode == 3:
            val = int(input("Enter your value: "))
            list[list[i + 1]] = val
            i += 2

        elif opcode == 4:
            print(ifirst)
            i += 2

        elif opcode == 5:
            i = isecond if ifirst != 0 else i + 3

        elif opcode == 6:
            i = isecond if ifirst == 0 else i + 3

        elif opcode == 7:
            list[list[i + 3]] = 1 if ifirst < isecond else 0
            i += 4

        elif opcode == 8:
            list[list[i + 3]] = 1 if ifirst == isecond else 0
            i += 4
        #list = list
    return list


file = readFile("input5")
operate(file)


'''
listeEqualto8pos = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
listeLessThanpos = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
listeEqualto8imm = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
listeLessThanimm = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
listejumppos = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
listejumpimm = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
listeLarge = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
              1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
              999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]

operated = operate(file)
print(operated)
'''
