import csv


def readFile(input):
    with open(input, newline='') as csvfile:
        data = list(csv.reader(csvfile))
        lista = []
        for x in data:
            for y in x:
                lista.append(y)
        lista = [int(i) for i in lista]
        return lista


def operate(list, x, thruster):
    i = ifirst = isecond = 0
    firstTime=1
    #amps = inputs
    #print("entering while with ampi:{0} and prevthrust:{1}".format(amps[ampi], thruster))
    while list[i] != 99:
        opcode = (lambda x: x % 100)(list[i])
        first_parameter = (lambda x, n: x // 10 ** n % 10)(list[i], 2)
        second_parameter = (lambda x, n: x // 10 ** n % 10)(list[i], 3)
        try:
            ifirst = list[i + 1] if first_parameter else list[list[i + 1]]
            isecond = list[i + 2] if second_parameter else list[list[i + 2]]
        except IndexError:
           # print("error")
            pass
        #print("opcode:{0}, i:{1}".format(opcode,i))

        if opcode == 1 or opcode == 2:
            list[list[i + 3]] = ifirst + isecond if opcode == 1 else ifirst * isecond
            i += 4

        elif opcode == 3:
            if firstTime:
                list[list[i + 1]] = x
                firstTime=0
            else:
                list[list[i + 1]] = thruster
            i += 2

        elif opcode == 4:
            thruster = ifirst
            #print(thruster)
            #print(ifirst)
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
    #print("operated")
    return thruster
    # return list
