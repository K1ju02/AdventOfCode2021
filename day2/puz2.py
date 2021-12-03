def solve():
    file = open("input2.txt")
    lines = file.readlines()
    forward = 0
    down = 0
    up = 0
    depth = 0
    for l in lines:
        inputs = l.split(" ")
        if inputs[0] == "forward":
            forward += int(inputs[1])
            depth += int(inputs[1]) * (down - up)
        elif inputs[0] == "down":
            down += int(inputs[1])
        else:
            up += int(inputs[1])
    return forward * depth

if __name__ == '__main__':
    print(solve())