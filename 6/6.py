'''
COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
'''
count = 0

listt = [
    ["COM", "B"],
    ["B", "C"],
    ["C", "D"],
    ["D", "E"],
    ["E", "F"],
    ["B", "G"],
    ["G", "H"],
    ["D", "I"],
    ["E", "J"],
    ["J", "K"],
    ["K", "L"],
]

in_orbit_around = {orbiter: target for (target, orbiter) in [line.split(')') for line in open('input6', 'r').read().splitlines()]}
get_distance_to = lambda orbiter, to: get_distance_to(in_orbit_around[orbiter], to) + 1 if orbiter != to else 0
print(sum(get_distance_to(orbiter, 'COM') for orbiter in in_orbit_around))

'''
class OrbitNode:
    def __init__(self, list):
        self.list = list
        self.data = list[-1][1]
        self.next = list[-1][0]
        return

    def has_value(self, value):
        if self.data == value:
            return True
        else:
            return False

    def listPrint(self):
        printval = self.


    def calc(self):
        print(self.data)
        print(self.next)





        #print(self.list[-1][1])


print(listt[-1])

orbits = OrbitNode(listt)
orbits.calc()
'''
