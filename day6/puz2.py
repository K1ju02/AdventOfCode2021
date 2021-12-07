import numpy as np

def solve():
    file = open("input6.txt")
    inputs = np.array(file.readline().split(","), dtype=int)
    fishes = np.zeros(9, dtype=np.int64)
    for n in inputs:
        fishes[n] += 1

    for i in range(256):
        fishes = np.roll(fishes, -1)
        fishes[6] += fishes[8]

    return np.sum(fishes)

if __name__ == '__main__':
    print(solve())