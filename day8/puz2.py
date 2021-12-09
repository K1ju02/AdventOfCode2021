import numpy as np

def wiring_contains_signal(string, check_list):
    res = [x for x in check_list if x in string]
    return bool(res)

def sort_str(stri):
    return "".join(sorted(stri))

def solve_8_2():
    file = open("input8.txt")
    lines = file.readlines()
    input_lines = []
    result = 0
    for line in lines:
        input_lines += [line.split("|")]
    for l in input_lines:
        l[0] = l[0].strip()
        l[1] = l[1].strip()
        signals = sorted(l[0].split(" "), key=len)
        digits = l[1].split(" ")
        output = ""
        solved = ["--"]*10
        solved[1] = sort_str(signals[0])
        solved[4] = sort_str(signals[2])
        solved[7] = sort_str(signals[1])
        solved[8] = sort_str(signals[-1])
        for i in range(len(signals)):
            current = sort_str(signals[i])
            if len(current) == 6:
                if all(c in current for c in solved[4]):
                    solved[9] = current
                elif all(c in current for c in solved[7]):
                    solved[0] = current
                else:
                    solved[6] = current
        for i in range(len(signals)):
            current = sort_str(signals[i])
            if len(current) == 5:
                if all(c in solved[9] for c in current):
                    if all(c in current for c in solved[7]):
                        solved[3] = current
                    else:
                        solved[5] = current
                else:
                    solved[2] = current
        for digit in digits:
            digit = sort_str(digit)
            for s in range(len(solved)):
                if digit == solved[s]:
                    output += str(s)
        result += int(output)
    return result

if __name__ == '__main__':
    print(solve_8_2())