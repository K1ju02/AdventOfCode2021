import numpy as np

def solve_day7_1():
    file = open("input7.txt")
    positions = np.array(file.readline().strip().split(","), dtype=int)
    m = np.median(positions)
    fuel = 0
    for pos in positions:
        fuel += abs(pos-m)
    return int(fuel)

if __name__ == '__main__':
    print(solve_day7_1())