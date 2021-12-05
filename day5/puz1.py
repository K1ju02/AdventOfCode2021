import numpy as np

def solve():
    file = open("input5.txt")
    lines = file.readlines()
    vents = np.zeros((1000,1000),dtype=np.int32)

    for line in lines:
        point1, point2 = line.split(" -> ")
        x1, y1 = point1.split(",")
        x2, y2 = point2.split(",")
        x1, y1, x2, y2 = int(x1.strip()), int(y1.strip()), int(x2.strip()), int(y2.strip())
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

    return np.count_nonzero(vents >= 2)

if __name__ == '__main__':
    print(solve())