import numpy as np
import puz1 as helper

def solve_13_2():
    file = open("input13.txt")
    lines = file.readlines()
    paper = np.zeros((1500, 1500), dtype=bool)
    for l in lines[:]:
        l.strip()
        cords = l.split(",")
        lines.remove(l)
        if len(cords) < 2:
            break
        x, y = cords
        paper[int(y)][int(x)] = True

    for l in lines:
        l.strip()
        leni = l.split('=')
        index = int(leni[1])
        axis = leni[0][-1]
        paper = helper.fold_axis(axis, paper, index)

    output = np.array(np.where(paper))
    grid = np.zeros((1+output[0].max(), 1+output[1].max()),dtype=int)
    print(output[0].max(), output[1].max())
    i = 0
    for x in output[0]:
        y = output[1][i]
        grid[x][y] = 1
        i += 1
    return '\n'.join(' '.join(str(x) for x in row) for row in grid)

if __name__ == '__main__':
    print(solve_13_2())