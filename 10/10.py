'''
.#..#
.....
#####
....#
...##
'''

file = open("input10e").read()
asteroids = []
x = y = 0

for elem in file:
    if elem == "#":
        asteroids.append([x, y])
    if x != 0 and x % 5 == 0:
        x = 0
        y += 1
    else:
        x += 1

for asteroid in asteroids:
    seen_asteroids = []
    for a in asteroids:
        relation = [a[0] - asteroid[0], a[1] - asteroid[1]]
        print("x: {0}, y:{1}".format(a[0], a[1]))
        print("x: {0}, y:{1}".format(relation[0], relation[1]))
        print()
        # print(relation)
        # print(a[0] + relation[0] and a[1] + relation[1])
        # print("x: {0}, y:{1}".format(a[0] + relation[0], a[1] + relation[1]))
        # if (a[0] + relation[0] and a[1] + relation[1] not in seen_asteroids):
        # seen_asteroids.append(a)
        # elif (a[0] - relation[0] and a[1] - relation[1] not in seen_asteroids):
        # seen_asteroids.append(a)
        # print()
        '''
        if a[0] - asteroid[0] == 0 or a[1] - asteroid[1] == 0:
            if 
            seen_asteroids.append(a)
        '''
    print()
    # seen_asteroids[0]
    # print("a:{0}, seen:{1}".format(asteroid,seen_asteroids))

# print(asteroids)
