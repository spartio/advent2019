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
firstTime = 1

def solve():
    counter=0
    while True:
        counter += 1
    #for _ in range(x):
        prevmoons = copy.deepcopy(moons)
        # prevmoons = moons
        # print("cur:{0},  vels:{1}".format(moons, velocities))
        # print("cur:{0},  prev:{1}".format(moons, prevmoons))
        buffers = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

        for a, b in itertools.combinations(moons, 2):
            for i in range(3):
                if a[i] < b[i]:
                    # print("a[i]:{0}, b[i]:{1}, a[i]-b[i]:{2}".format(a[i],b[i], a[i]+b[i]))
                    buffers[i][moons.index(a)] += 1
                    buffers[i][moons.index(b)] += -1
                elif a[i] > b[i]:
                    buffers[i][moons.index(a)] += -1
                    buffers[i][moons.index(b)] += 1
            # print(buffers)
        # print(buffers)
        for i in range(4):
            for j in range(3):
                # print(buffers[j][i])
                # prevmoons[i][j] = moons[i][j]
                moons[i][j] += buffers[j][i]
                moons[i][j] += velocities[i][j]
                velocities[i][j] = moons[i][j] - prevmoons[i][j]
                #print("moons[i][j]:{0} - prevmoons[i][j]:{1} = velocities:{2}".format(moons[i][j], prevmoons[i][j],
                 #                                                                     velocities[i][j]))
                # velocities[i][j] = buffers[j][i]

                # moons[0] +=  buffers[moon]
        print(counter)

        if moons==prevmoons:
            break
    summ=0
    for pot, kin in zip(moons, velocities):
        pot = [abs(x) for x in pot]
        kin = [abs(x) for x in kin]
        summ+=sum(pot) * sum(kin)
        print(summ)
    print(counter)

    print(moons)
        # print("prev", prevmoons)
        # print("prev:{0}".format(prevmoons))
        # print("cur:{0},  vels:{1}".format(moons, velocities))
    # return moons


# print(velocities)
# print(buffers)
# print(moons)

solve()

# solve()
# solve()
