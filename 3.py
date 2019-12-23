'''
s1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
s1 = s1.split(',')
s2 = "U62,R66,U55,R34,D71,R55,D58,R83"
s2 = s2.split(',')
'''



def calc(path):
    curx = cury = step = 0
    directions = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
    points = {}
    for segment in path:
        dx, dy = directions[segment[0]]
        for _ in range(int(segment[1:])):
            curx += dx
            cury += dy
            step += 1
            if (curx, cury) not in points:
                points[(curx, cury)] = step
    return points


s1_points = calc(s1)
s2_points = calc(s2)
intersection_points = [point for point in s1_points if point in s2_points]

part1 = min(abs(x) + abs(y) for (x, y) in intersection_points)

print(part1)