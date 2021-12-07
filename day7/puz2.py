import numpy as np

def triangle_num(n):
    res = 0
    for i in range(n+1):
        res += i
    return res

def solve_day7_2():
    file = open("input7.txt")
    positions = np.array(file.readline().strip().split(","), dtype=int)
    m = int(np.mean(positions))
    print(m)
    fuel = 0
    for pos in positions:
        fuel += triangle_num(abs((pos-m)))
    return fuel

if __name__ == '__main__':
    print(solve_day7_2())