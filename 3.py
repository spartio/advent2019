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

lines = open("input3").read().splitlines()
s1 = lines[0].split(',')
s2 = lines[1].split(',')


s1_points = calc(s1)
s2_points = calc(s2)
intersection_points = [point for point in s1_points if point in s2_points]

part1 = min(abs(x) + abs(y) for (x, y) in intersection_points)
part2 = min(s1_points[point] + s2_points[point] for point in intersection_points)
print('Part 1: {0}, Part 2: {1}'.format(part1, part2))