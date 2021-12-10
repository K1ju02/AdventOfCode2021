import numpy as np

def find_illegals(line, res):
    queue = []
    for s in line:
        if s in ')':
            x = queue.pop()
            if x not in '(':
                res += 3
                queue = []
                break
        elif s in ']':
            x = queue.pop()
            if x not in '[':
                res += 57
                queue = []
                break
        elif s in '}':
            x = queue.pop()
            if x not in '{':
                res += 1197
                queue = []
                break
        elif s in '>':
            x = queue.pop()
            if x not in '<':
                res += 25137
                queue = []
                break
        else:
            queue.append(s)
    return res, queue

def solve_10_1():
    file = open("input10.txt")
    lines = file.readlines()
    res = 0
    for line in lines:
        line = line.strip()
        res = find_illegals(line, res)
    return res


if __name__ == '__main__':
    print(solve_10_1())