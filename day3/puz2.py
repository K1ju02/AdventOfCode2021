def convert_to_binary(bits):
    result = 0
    power = len(bits)-1
    for digit in bits:
        result += int(digit) * (2 ** power)
        power -= 1
    return result

def solve():
    file = open("input3.txt")
    lines = file.readlines()
    lines_oxy = lines
    lines_co = lines

    for i_oxy in range(len(lines_oxy[0].strip())):
        if len(lines_oxy) == 1:
            break
        sum_one, sum_zero = find_sums(i_oxy, lines_oxy)
        if sum_one >= sum_zero:
            lines_oxy = [item for item in lines_oxy if int(item.strip()[i_oxy]) == 1]
        else:
            lines_oxy = [item for item in lines_oxy if int(item.strip()[i_oxy]) == 0]
        i_oxy += 1

    for i_co in range(len(lines_co[0].strip())):
        if len(lines_co) == 1:
            break
        sum_one, sum_zero = find_sums(i_co, lines_co)

        if sum_one < sum_zero:
            lines_co = [item for item in lines_co if int(item.strip()[i_co]) == 1]
        else:
            lines_co = [item for item in lines_co if int(item.strip()[i_co]) == 0]
        i_co += 1

    oxygen = convert_to_binary(lines_oxy[0].strip())
    co2 = convert_to_binary(lines_co[0].strip())

    return oxygen * co2


def find_sums(i, lines):
    sum_one = 0
    sum_zero = 0
    for n in range(len(lines)):
        int_at_co = int(lines[n][i].strip())
        if int_at_co:
            sum_one += 1
        else:
            sum_zero += 1
        n += 1
    return sum_one, sum_zero

if __name__ == '__main__':
    print(solve())


