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