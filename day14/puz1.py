from collections import Counter
import numpy as np

def poly_insert(string, rules, i):
    if i < 1:
        return string
    insert = []
    for j in range(len(string)-1):
        for rule in rules:
            if string[j:j+2] in rule[0]:
                insert.append((j+1, rule[1].strip()))
    insert.reverse()
    for x in insert:
        string = string[:x[0]] + x[1] + string[x[0]:]
    print("step", i, string)
    i -= 1
    return poly_insert(string, rules, i)

def solve_14_1():
    file = open("input14t.txt")
    first_line = file.readline().strip()
    file.readline()
    lines = file.readlines()
    rules = []
    for l in lines:
        rules += [l.split(" -> ")]
    print(rules)
    output = poly_insert(first_line, rules, 10)
    counts = Counter(output)
    count_max = max(counts, key= lambda x: counts[x])
    count_min = min(counts, key= lambda x: counts[x])
    return output.count(count_max) - output.count(count_min)

if __name__ == '__main__':
    print(solve_14_1())