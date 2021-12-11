import numpy as np
import puz1 as helpo

def solve_11_2():
    file = open("input11.txt")
    lines = file.readlines()
    octopuses = []
    for line in lines:
        line = line.strip()
        for c in line:
            octopuses += [int(c)]
    octopuses = np.reshape(octopuses, (10,10))
    i = 1
    flash_count = 0
    while i <= 999:
        octopuses += 1
        print("step", i)
        flash = np.zeros((10, 10), dtype=bool)
        for x in range(len(octopuses)):
            for y in range(len(octopuses[0])):
                octopuses, flash, flash_count = helpo.energy_step(octopuses, (x, y), flash, flash_count)
        if not np.sum(octopuses):
            return i
        print(octopuses)
        i += 1

if __name__ == '__main__':
    print(solve_11_2())