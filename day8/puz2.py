import numpy as np

def wiring_contains_signal(string, check_list):
    res = [x for x in check_list if x in string]
    return bool(res)

def solve_8_2():
    file = open("input8t.txt")
    lines = file.readlines()
    input_lines = []
    for line in lines:
        input_lines += [line.split("|")]
    for l in input_lines:
        wiring = [["a","b","c","d","e","f", "g"]]*7
        l[0] = l[0].strip()
        l[1] = l[1].strip()
        signals = sorted(l[0].split(" "), key=len)
        digits = l[1].split(" ")
        for i in range(len(wiring)):
            if i == 2 or i == 5:
                wiring[i] = [s for s in wiring[i] if signals[0].__contains__(s)]
            else:
                wiring[i] = [s for s in wiring[i] if not signals[0].__contains__(s)]
        print(wiring)
        for i in range(len(wiring)):
            if i == 0 or i == 2 or i == 5:
                wiring[i] = [s for s in wiring[i] if signals[1].__contains__(s)]
            else:
                wiring[i] = [s for s in wiring[i] if not signals[1].__contains__(s)]
        print(wiring)
        for i in range(len(wiring)):
            if 1 <= i <= 3 or i == 5:
                wiring[i] = [s for s in wiring[i] if signals[2].__contains__(s)]
            else:
                wiring[i] = [s for s in wiring[i] if not signals[2].__contains__(s)]
        print(wiring)
        #for i in range(6, 9):

        #for i in range(3, 5):

        #if i == 5:
        #    wiring[i] = [s for s in wiring[i] if not signals[].__contains__(s)]
        #else:
        #    wiring[i] = [s for s in wiring[i] if signals[].__contains__(s)]
        #print(wiring)

    return

if __name__ == '__main__':
    print(solve_8_2())