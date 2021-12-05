import numpy as np
import day5.puz1 as help
from matplotlib import pyplot
from matplotlib import colors

def solve():
    file = open("input5.txt")
    lines = file.readlines()
    vents = np.zeros((1000, 1000), dtype=np.int32)

    for line in lines:
        x1, y1, x2, y2 = help.split_line_to_cords(line)
        if x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1
            for i in range(abs(y1 - y2)+1):
                vents[y1+i][x1] += 1
        elif y1 == y2:
            if x1 > x2:
                x1, x2 = x2, x1
            for i in range(abs(x1 - x2)+1):
                vents[y1][x1+i] += 1
        elif y1 < y2:
            if x1 < x2:
                for i in range(y2-y1+1):
                    vents[y1+i][x1+i] += 1
            else:
                for i in range(y2-y1+1):
                    vents[y1+i][x1-i] += 1
        else:
            if x1 < x2:
                for i in range(abs(y2-y1)+1):
                    vents[y1-i][x1+i] += 1
            else:
                for i in range(abs(y2-y1)+1):
                    vents[y1-i][x1-i] += 1

    pyplot.figure(figsize=(50, 50))
    pyplot.imshow(vents)
    pyplot.show()
    return np.count_nonzero(vents >= 2)


if __name__ == '__main__':
    print(solve())

