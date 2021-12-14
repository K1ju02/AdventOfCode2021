import copy


def poly_smart(string, rules, i):
    pairs = dict()
    for c in range(len(string)-1):
        if string[c:c+2] in pairs:
            pairs[string[c:c+2]] += 1
        else:
            pairs[string[c:c + 2]] = 1
    for j in range(i):
        new_pairs = copy.deepcopy(pairs)
        for r in rules:
            sol = rules[r]
            if r in pairs:
                val = pairs[r]
                new_pairs[r] -= val
                if r[0]+sol in new_pairs:
                    new_pairs[r[0]+sol] += val
                else:
                    new_pairs[r[0]+sol] = val
                if sol+r[1] in new_pairs:
                    new_pairs[sol+r[1]] += val
                else:
                    new_pairs[sol+r[1]] = val
        pairs = copy.deepcopy(new_pairs)
    return pairs

def solve_14_2():
    file = open("input14.txt")
    first_line = file.readline().strip()
    file.readline()
    lines = file.readlines()
    rules = dict()
    for l in lines:
        current = l.split(" -> ")
        rules[current[0]] = current[1].strip()
    print(rules)
    out = poly_smart(first_line, rules, 40)
    char_count = dict()
    print(out)
    print(sum(out.values()))
    for key in out:
        x, y = key
        if x in char_count:
            char_count[x] += out[key]
        else:
            char_count[x] = out[key]
    char_count[first_line[-1]] += 1
    print(char_count)
    max_count = max(x for x in char_count.values())
    print(max_count)
    min_count = min(x for x in char_count.values() if x > 0)
    print(min_count)

    return max_count-min_count

if __name__ == '__main__':
    print(solve_14_2())