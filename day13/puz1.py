import numpy as np

def fold_axis(axis, paper, index):
    if axis in 'x':
        for i in range(len(paper)):
            j = index
            for n in range(index, len(paper[0])):
                #print("x:",j)
                if j < 0: break
                paper[i][j] = paper[i][n] or paper[i][j]
                paper[i][n] = False
                j -= 1
    else:
        for n in range(len(paper[0])):
            j = index
            for i in range(index, len(paper)):
                #print("y:",j)
                if j < 0: break
                paper[j][n] = paper[i][n] or paper[j][n]
                paper[i][n] = False
                j -= 1
    return paper

def solve_13_1():
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
    lines[0].strip()
    line = lines[0].split('=')
    index = int(line[1])
    axis = line[0][-1]
    paper = fold_axis(axis, paper, index)

    return np.sum(paper)

if __name__ == '__main__':
    print(solve_13_1())