import numpy as np

#mostly from SO
#https://stackoverflow.com/questions/51657128/how-to-access-the-adjacent-cells-of-each-elements-of-matrix-in-python
def get_adj(arr2d, cords):
    adj = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            range_x = range(0, arr2d.shape[0])  # X bounds
            range_y = range(0, arr2d.shape[1])  # Y bounds

            (newX, newY) = (cords[0] + dx, cords[1] + dy)  # adjacent cell

            if (newX in range_x) and (newY in range_y) and (dx, dy) != (0, 0):
                adj.append((newX, newY))
    return adj

def energy_step(octo, cords, flash, flash_count):
    x, y = cords
    if octo[x][y] > 9:
        flash[x][y] = True
        octo[x][y] = 0
        flash_count += 1
        positions = get_adj(octo, cords)
        for pos in positions:
            print(flash[pos[0]][pos[1]])
            if not flash[pos[0]][pos[1]]:
                octo[pos[0]][pos[1]] += 1
                octo, flash, flash_count = energy_step(octo, pos, flash, flash_count)
    return octo, flash, flash_count

def solve_11_1():
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
    while i <= 100:
        octopuses += 1
        print("step", i)
        flash = np.zeros((10, 10), dtype=bool)
        for x in range(len(octopuses)):
            for y in range(len(octopuses[0])):
                octopuses, flash, flash_count = energy_step(octopuses, (x, y), flash, flash_count)
        print(octopuses)
        i += 1
    return flash_count

if __name__ == '__main__':
    print(solve_11_1())