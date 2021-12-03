def solve():
    file = open("input3.txt")
    lines = file.readlines()
    rows = []
    bits = []
    gamma = 0
    epsilon = 0

    for i in range(len(lines[0])-1):
        cols = []
        for n in range(len(lines)-1):
            cols += [int(lines[n].strip()[i])]
        rows += [cols]
    for a in rows:
        sum_one = a.count(1)
        if sum_one > len(a)/2:
            bits += [1]
        else:
            bits += [0]
    power = len(bits)-1

    for digit in bits:
        gamma += digit * (2 ** power)
        epsilon += int(not digit) * (2 ** power)
        power -= 1

    return gamma * epsilon

if __name__ == '__main__':
        print(solve())