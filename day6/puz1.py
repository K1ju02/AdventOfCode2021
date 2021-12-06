import numpy as np

def solve():
    file = open("input6.txt")
    inputs = np.array(file.readline().split(","), dtype=np.int8)

    for i in range(80):
        for n in range(len(inputs)):
            if inputs[n] > 0:
                inputs[n] += -1
            else:
                inputs[n] = 6
                inputs = np.append(inputs, [8])
        print("day ", i, inputs)

    return len(inputs)

if __name__ == '__main__':
    print(solve())