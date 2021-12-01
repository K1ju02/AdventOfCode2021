def solve():
    input_f = open('input1.txt')
    readings = input_f.readlines()
    ints = []
    for s in readings:
        s.strip()
        ints += [int(s)]
    count = 0
    size = range(len(ints))
    for x in size:
        if x + 3 > len(size):
            break
        if ints[x] + ints[x+1] + ints[x+2] > ints[x-1] + ints[x] + ints[x+1]:
            count += 1
    return count


if __name__ == '__main__':
    print(solve())