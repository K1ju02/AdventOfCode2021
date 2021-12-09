import numpy as np

def solve_8_1():
    file = open("input8.txt")
    lines = file.readlines()
    digits = []
    for line in lines:
        digits += line.split("|")[1].split(" ")

    count = 0
    for digit in digits:
        digit = digit.strip()
        if 2 <= len(digit) <= 4 or len(digit) == 7:
            count += 1
    return count

if __name__ == '__main__':
    print(solve_8_1())