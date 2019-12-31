from imports.imports import readFile


lista = readFile("input2")


def operate(list):
    i = 0
    while list[i] != 99:
        if list[i] == 1:
            list[list[i + 3]] = list[list[i + 1]] + list[list[i + 2]]
        elif list[i] == 2:
            list[list[i + 3]] = list[list[i + 1]] * list[list[i + 2]]
        i = i + 4
        list = list
    return list


def operate2():
    asdlol = 0
    total = 19690720
    lis = lista
    for i in range(0, 100):
        for j in range(0, 100):
            lis = readFile("input2")
            lis[1] = j
            lis[2] = i
            operate(lis)
            if lis[0] == total:
                asdlol1 = lis[1]
                asdlol2 = lis[2]
                print("{0}, {1}".format(asdlol1,asdlol2))
                return asdlol


print(operate(lista)[0])
operate2()