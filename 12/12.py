'''
<x=-10, y=-10, z=-13>
<x=5, y=5, z=-9>
<x=3, y=8, z=-16>
<x=1, y=3, z=-3>
'''
from re import findall
import itertools
import copy

lines = open("input12ee").read().splitlines()


def extract_ints(line):
    return [int(x) for x in findall(r'-?\d+', line)]


moons = [extract_ints(line) for line in lines]
initial = copy.deepcopy(moons)

velocities = [[0 for x in range(3)] for y in range(4)]


def solve(x):
    counter=0
    for _ in range(x):
    #while True:
        counter += 1
        prevmoons = copy.deepcopy(moons)
        buffers = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

        for a, b in itertools.combinations(moons, 2):
            for i in range(3):
                if a[i] < b[i]:
                    buffers[i][moons.index(a)] += 1
                    buffers[i][moons.index(b)] += -1
                elif a[i] > b[i]:
                    buffers[i][moons.index(a)] += -1
                    buffers[i][moons.index(b)] += 1
        for i in range(4):
            for j in range(3):
                moons[i][j] += buffers[j][i] + velocities[i][j]
                velocities[i][j] = moons[i][j] - prevmoons[i][j]
        if moons==prevmoons:
            break
    summ=0
    for pot, kin in zip(moons, velocities):
        pot = [abs(x) for x in pot]
        kin = [abs(x) for x in kin]
        summ += sum(pot) * sum(kin)
        print(summ)
    print(moons)


solve(50)

