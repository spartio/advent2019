from imports.imports import readFile

file = readFile("input5")
print(file)

liste = [1002, 4, 3, 4, 33]
liste2 = [1101, 100, -1, 4, 0]


def get_digit(number, n):
    return number // 10 ** n % 10


def get_opcode(number):
    return number % 100


def operate(list):
    i = 0
    while list[i] != 99:
        if list[i] > 99:
            opcode = get_opcode(list[i])
            first_parameter = get_digit(list[i], 2)
            second_parameter = get_digit(list[i], 3)
            third_parameter = get_digit(list[i], 4)
            print("i:{0}, opcode:{1}, first:{2}, second:{3}, third:{4}".format(list[i], opcode, first_parameter,
                                                                               second_parameter, third_parameter))
            if opcode == 1:
                # print("eka")
                list[list[i + 3]] = (list[i + 1] if first_parameter else list[list[i + 1]]) + (list[
                                                                                                   i + 2] if second_parameter else
                                                                                               list[list[i + 2]])
                # list[list[i + 3]] = list[list[i + 1]] if first_parameter else list[i + 1] + list[list[i + 2]] if second_parameter else list[i + 2]
                # list[list[i+3]] = if first_parameter list[list[i + 1]]
                # list[list[i + 3]] = list[list[i + 1]] + list[list[i + 2]]
                i = i + 4
            elif opcode == 2:
                list[list[i + 3]] = (list[i + 1] if first_parameter else list[list[i + 1]]) * (list[
                                                                                                   i + 2] if second_parameter else
                                                                                               list[list[i + 2]])
                # list[list[i + 3]] = list[list[i + 1]] if first_parameter else list[i + 1] * list[list[i + 2]] if second_parameter else list[i + 2]
                # list[list[i + 3]] = list[list[i + 1]] * list[list[i + 2]]
                i = i + 4
            elif opcode == 3:
                val = int(input("Enter your value: "))
                # print("asd")
                list[list[i + 1]] = val
                i = i + 2
                # print(file[225])
            elif opcode == 4:
                print(list[list[i + 1]])
                i = i + 2
            # else:
        # print("error: {0}".format(list[i]))
        else:
            opcode = get_opcode(list[i])
            if opcode == 1:
                list[list[i + 3]] = list[list[i + 1]] + list[list[i + 2]]
                i = i + 4
            elif opcode == 2:
                list[list[i + 3]] = list[list[i + 1]] * list[list[i + 2]]
                i = i + 4
            elif opcode == 3:
                val = int(input("Enter your value: "))
                list[list[i + 1]] = val
                i = i + 2
            elif opcode == 4:
                print(list[list[i + 1]])
                i = i + 2
        list = list
    return list


def operate2(list):
    i = 0
    while list[i] != 99:
        if list[i] > 99:
            opcode = get_opcode(list[i])
            first_parameter = get_digit(list[i], 2)
            second_parameter = get_digit(list[i], 3)
            third_parameter = get_digit(list[i], 4)
            print("i:{0}, opcode:{1}, first:{2}, second:{3}, third:{4}".format(list[i], opcode, first_parameter,
                                                                               second_parameter, third_parameter))
            if opcode == 1:
                list[list[i + 3]] = (list[i + 1] if first_parameter else list[list[i + 1]]) + (list[
                                                                                                   i + 2] if second_parameter else
                                                                                               list[list[i + 2]])
                i = i + 4
            elif opcode == 2:
                list[list[i + 3]] = (list[i + 1] if first_parameter else list[list[i + 1]]) * (list[
                                                                                                   i + 2] if second_parameter else
                                                                                               list[list[i + 2]])
                i = i + 4
            elif opcode == 3:
               val = int(input("Enter your value: "))
               list[list[i + 1]] = val
               i = i + 2

            elif opcode == 4:
                if first_parameter:
                    print(list[i + 1])
                else:
                    print(list[list[i + 1]])

                i = i + 2

            elif opcode == 5:
                if first_parameter and second_parameter:
                    i = list[i + 2] if (list[i + 1] != 0) else (i + 3)
                elif first_parameter and not second_parameter:
                    i = list[list[i + 2]] if (list[i + 1] != 0) else (i + 3)
                elif not first_parameter and second_parameter:
                    i = list[i + 2] if (list[list[i + 1]] != 0) else (i + 3)
                else:
                    i = list[list[i + 2]] if (list[list[i + 1]] != 0) else (i + 3)

#list[list[i + 3]] = (list[i + 1] if first_parameter else list[list[i + 1]]) + (list[i + 2] if second_parameter else list[list[i + 2]])
            elif opcode == 6:
                if first_parameter and second_parameter:
                    i = list[i + 2] if list[i + 1] == 0 else (i + 3)
                elif first_parameter and not second_parameter:
                    i = list[list[i + 2]] if list[i + 1] == 0 else (i + 3)
                elif not first_parameter and second_parameter:
                    i = list[i + 2] if list[list[i + 1]] else (i + 3)
                else:
                    i = list[list[i + 2]] if list[list[i + 1]] == 0 else (i + 3)

            elif opcode == 7:
                if first_parameter and second_parameter:
                    list[list[i + 3]] = 1 if (list[i + 1] < list[i + 2]) else 0
                elif first_parameter and not second_parameter:
                    list[list[i + 3]] = 1 if (list[i + 1] < list[list[i + 2]]) else 0
                elif not first_parameter and second_parameter:
                    list[list[i + 3]] = 1 if (list[list[i + 1]] < list[i + 2]) else 0
                else:
                    list[list[i + 3]] = 1 if (list[list[i + 1]] < list[list[i + 2]]) else 0
                i = i + 4

            elif opcode == 8:
                if first_parameter and second_parameter:
                    list[list[i + 3]] = 1 if (list[i + 1] == list[i + 2]) else 0
                elif first_parameter and not second_parameter:
                    list[list[i + 3]] = 1 if (list[i + 1] == list[list[i + 2]]) else 0
                elif not first_parameter and second_parameter:
                    list[list[i + 3]] = 1 if (list[list[i + 1]] == list[i + 2]) else 0
                else:
                    list[list[i + 3]] = 1 if (list[list[i + 1]] == list[list[i + 2]]) else 0
                i = i + 4
        else:
            opcode = get_opcode(list[i])
            print("i:{0}, opcode:{1}".format(list[i], opcode))

            if opcode == 1:
                list[list[i + 3]] = list[list[i + 1]] + list[list[i + 2]]
                i = i + 4
            elif opcode == 2:
                list[list[i + 3]] = list[list[i + 1]] * list[list[i + 2]]
                i = i + 4

            if opcode == 3:
                val = int(input("Enter your value: "))
                list[list[i + 1]] = val
                i = i + 2

            elif opcode == 4:
                print(list[list[i + 1]])
                i = i + 2

            elif opcode == 5:
                i = list[list[i + 2]] if (list[list[i + 1]] != 0) else (i + 3)
                #if list[list[i + 1]] != 0:
                #    i = list[list[i + 2]]
                #else:
                #    i = i + 3
            elif opcode == 6:
                i = list[list[i + 2]] if (list[list[i + 1]] == 0) else (i + 3)
                #if list[list[i + 1]] == 0:
                #    i = list[list[i + 2]]
                #else:
                #    i = i + 3
            elif opcode == 7:
                list[list[i + 3]] = 1 if (list[list[i + 1]] < list[list[i + 2]]) else 0
                i = i + 4
                #if list[list[i + 1]] < list[list[i + 2]]:
                ##    list[list[i + 3]] = 1
                #else:
                #    list[list[i + 3]] = 0
                #i = i + 4
            elif opcode == 8:
                list[list[i + 3]] = 1 if (list[list[i + 1]] == list[list[i + 2]]) else 0
                i = i + 4
                #if list[list[i + 1]] == list[list[i + 2]]:
                ##    list[list[i + 3]] = 1
                #else:
                #    list[list[i + 3]] = 0

        list = list
    return list


listeEqualto8pos = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
listeLessThanpos = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
listeEqualto8imm = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
listeLessThanimm = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
listejumppos = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
listejumpimm = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
listeLarge = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
              1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
              999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]

operated = operate2(listeLarge)
#print(operate2(listeEqualto8pos))
#print(operate2(listeEqualto8imm))
#print(operate2(listeLessThanpos))
#print(operate2(listeLessThanimm))

#print(operate2(listejumppos))
#print(operate2(listejumpimm))
print(operated)

'''
opcode = get_opcode(liste2[0])
first_parameter = get_digit(liste2[0], 2)
second_parameter = get_digit(liste2[0], 3)
third_parameter = get_digit(liste2[0], 4)
print(liste2)
print("i:{0}, opcode:{1}, first:{2}, second:{3}, third:{4}".format(liste2[0], opcode, first_parameter,
                                                                   second_parameter, third_parameter))
liste2[liste2[3]] = (liste2[1] if first_parameter else liste2[liste2[1]]) + (liste2[
    2] if second_parameter else liste2[liste2[2]])
print(liste2)
'''
