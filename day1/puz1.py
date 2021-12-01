def solve():
    input_f = open('input1.txt')
    readings = input_f.readlines()
    ints = []
    for s in readings:
        s.strip()
        ints += [int(s)]
    count = 0
    for x in range(len(ints)):
        if ints[x] > ints[x-1]:
            count += 1
    return count




if __name__ == '__main__':
    print(solve())