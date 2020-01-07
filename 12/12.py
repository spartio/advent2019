'''
<x=-10, y=-10, z=-13>
<x=5, y=5, z=-9>
<x=3, y=8, z=-16>
<x=1, y=3, z=-3>
'''
from re import findall
import itertools

lines = open("input12").read().splitlines()


def extract_ints(line):
    return [int(x) for x in findall(r'-?\d+', line)]


prevmoons = moons = [extract_ints(line) for line in lines]
velocities = [[0 for x in range(3)] for y in range(4)]
firstTime = 1

def solve(x, prevmoons):

    for _ in range(x):
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
        #print(buffers)
        for i in range(4):
            for j in range(3):
                # print(buffers[j][i])
                prevmoons[i][j] = moons[i][j]
                moons[i][j] += buffers[j][i]

                velocities[i][j] = buffers[j][i]

                # moons[0] +=  buffers[moon]

        if firstTime:
            firstTime = 0
        else:
            for i in range(4):
                for j in range(3):
                    moons[i][j] += velocities[i][j]

        print("prev", prevmoons)
        print("cur", moons)
    return moons
# print(velocities)
# print(buffers)
# print(moons)

solve(2)

# solve()
# solve()
