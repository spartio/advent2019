from imports.imports import readFile, operate2

file = readFile("input11")

tiles = []
directions = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}


def paint_execute(code, initial_color):
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    program = operate2(code)
    x = y = direction = 0
    panel = {(x, y): initial_color}
    while not program.halted:
        program.input(panel[(x, y)] if (x, y) in panel else 0)
        output1 = program.run()
        output2 = program.run()
        if not program.halted:
            panel[(x, y)] = output1
            direction = ((direction + 1) if output2 == 1 else (direction - 1 + len(directions))) % len(directions)
            x, y = x + directions[direction][0], y + directions[direction][1]
    return panel


print(paint_execute(file,0))


def paint(list):
    i = ifirst = isecond = curx = cury = 0
    dir = 'U'
    times = 0
    val = -2
    while list[i] != 99:
        opcode = (lambda x: x % 100)(list[i])
        first_parameter = (lambda x, n: x // 10 ** n % 10)(list[i], 2)
        second_parameter = (lambda x, n: x // 10 ** n % 10)(list[i], 3)
        try:
            ifirst = list[i + 1] if first_parameter else list[list[i + 1]]
            isecond = list[i + 2] if second_parameter else list[list[i + 2]]
        except IndexError:
            pass

        if opcode == 1 or opcode == 2:
            list[list[i + 3]] = ifirst + isecond if opcode == 1 else ifirst * isecond
            i += 4

        elif opcode == 3:
            val = int(input("Enter your value: "))
            list[list[i + 1]] = val
            print(tiles)
            i += 2

        elif opcode == 4:
            if times % 2 == 0:
                tiles.append([[curx, cury], val])
            # else:
            #    if ifirst==1:

            curx += directions[dir]
            cury += directions[dir]

            # print(ifirst)
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
    return list
# paint(file)
