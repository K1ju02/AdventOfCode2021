import numpy as np
import puz1 as helper

def solve_10_2():
    file = open("input10.txt")
    lines = file.readlines()
    end = []
    for line in lines:
        line.strip()
        res, queue = helper.find_illegals(line, 0)
        res = []
        for i in range(len(queue)):
            item = queue.pop()
            if item in '(':
                res += [')']
            elif item in '[':
                res += [']']
            elif item in '{':
                res += ['}']
            elif item in '<':
                res += ['>']
        count = 0
        for br in res:
            count *= 5
            if br in ')':
                count += 1
            elif br in ']':
                count += 2
            elif br in '}':
                count += 3
            elif br in '>':
                count += 4
        if count > 0:
            end += [count]
    return int(np.median(end))

if __name__ == '__main__':
    print(solve_10_2())
